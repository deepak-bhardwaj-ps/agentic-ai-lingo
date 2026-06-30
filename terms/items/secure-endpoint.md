---
title: Secure endpoint
short_description: A network endpoint designed to reduce the risk of eavesdropping, tampering, and unauthorised access.
category: Protocols
tags:
- networking
- security
- protocols
status: reviewed
aliases: []
meaning_type: overloaded_buzzword
novelty_level: low
maturity_level: maturing
common_misuse:
- Treating it as a formal technical standard when it is usually just a plain-language label.
- Assuming it means only HTTPS, when it can also imply certificates, authentication, and access controls.
related_terms:
- API endpoint
- HTTPS
- TLS
- mutual TLS
- certificate
- service endpoint
evidence:
  - source_title: Request endpoints
    source_url: https://docs.cloud.google.com/storage/docs/request-endpoints
    source_type: official_docs
    relevance: Shows that an endpoint is simply the URL or network location where a service can be accessed, which is the base meaning behind the term.
    key_point: Google Cloud defines an endpoint as the location where Cloud Storage can be accessed, written as a URL.
  - source_title: The Transport Layer Security (TLS) Protocol Version 1.3
    source_url: https://datatracker.ietf.org/doc/html/rfc8446
    source_type: standards_doc
    relevance: Provides the security layer that usually makes an endpoint secure by protecting traffic in transit.
    key_point: TLS is designed to prevent eavesdropping, tampering, and message forgery between client and server.
  - source_title: Create an HTTPS listener for your Application Load Balancer
    source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html
    source_type: official_docs
    relevance: Shows how a secure endpoint is commonly implemented in practice with certificates and HTTPS/TLS configuration.
    key_point: AWS requires a server certificate and a security policy for an HTTPS listener, and uses the certificate to terminate and decrypt client connections.
---
An endpoint is the address where a service can be reached. A secure endpoint is an endpoint set up so traffic is protected, usually with HTTPS or TLS, and often with a certificate and access checks.

In practice, this means the data sent to and from the service is harder to read or change while it travels over the network. The server also proves its identity with a certificate, which helps stop fake sites or services from pretending to be real ones.

The term matters because it is a simple way to say that a service should not be left open or plain-text on the internet. A secure endpoint is safer than an unprotected one, but security still depends on how it is configured.

This is not a formal standard term. It does not always mean the same thing in every product or team, and it does not guarantee that the service is fully safe. It usually does not mean “secure by default”; it only describes one part of the system.
