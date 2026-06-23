#!/usr/bin/env node
import fs from 'node:fs/promises';
import path from 'node:path';
import { spawn } from 'node:child_process';

const repoRoot = process.argv[2] ? path.resolve(process.argv[2]) : process.cwd();
const progressPath = path.join(repoRoot, 'progress.json');
const termsDir = path.join(repoRoot, 'terms', 'items');
const codexBin = process.env.CODEX_BIN || 'codex';
const codexModel = process.env.CODEX_MODEL || 'gpt-5.4-mini';

const writerInstructions = await fs.readFile(path.join(repoRoot, '.codex', 'agents', 'agentic-research-writer.md'), 'utf8');
const editorInstructions = await fs.readFile(path.join(repoRoot, '.codex', 'agents', 'agentic-senior-editor.md'), 'utf8');
const skillInstructions = await fs.readFile(path.join(repoRoot, '.codex', 'skills', 'rewrite-agentic-terms', 'SKILL.md'), 'utf8');

async function readProgress() {
  return JSON.parse(await fs.readFile(progressPath, 'utf8'));
}

async function listTerms() {
  return (await fs.readdir(termsDir))
    .filter((name) => name.endsWith('.md'))
    .sort()
    .map((name) => path.join('terms', 'items', name));
}

function runCodex(prompt) {
  return new Promise((resolve, reject) => {
    const child = spawn(codexBin, ['exec', '--model', codexModel, '--cd', repoRoot, '--sandbox', 'workspace-write', '--ask-for-approval', 'never', prompt], {
      stdio: ['ignore', 'inherit', 'inherit'],
      env: process.env,
    });
    child.on('exit', (code) => {
      if (code === 0) resolve();
      else reject(new Error(`codex exec failed with exit code ${code}`));
    });
  });
}

const progress = await readProgress();
const completed = new Set(progress.completed ?? []);
const allTerms = await listTerms();
const remaining = allTerms.filter((term) => !completed.has(term));

for (const term of remaining) {
  const termPath = path.join(repoRoot, term);
  const content = await fs.readFile(termPath, 'utf8');
  const prompt = [
    'Use the rewrite-agentic-terms skill and the two agent instructions below.',
    'Work on exactly one glossary term: ' + term,
    '',
    'Skill:',
    skillInstructions.trim(),
    '',
    'Research writer instructions:',
    writerInstructions.trim(),
    '',
    'Senior editor instructions:',
    editorInstructions.trim(),
    '',
    'Current term file content:',
    content.trim(),
    '',
    'Task:',
    'Research the term, rewrite the entire file, preserve YAML frontmatter schema, avoid generic openings, and update any sources needed to support the definition.',
    'Do not process any other file.',
  ].join('\n');

  await runCodex(prompt);
}
