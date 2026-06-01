# News Digest Agent for Telegram & Slack

A local-first template for building scheduled Telegram/Slack digest bots for any topic.

## What it does

This project helps you build a digest bot that:

- monitors selected sources
- extracts relevant updates
- filters and scores items
- generates a short digest
- sends it to Telegram or Slack
- runs on a schedule

## Use cases

- industry news digests
- competitor monitoring
- regulatory updates
- security advisories
- product release monitoring
- grant and funding alerts
- research paper digests
- newsletter summaries

## Core idea

Instead of asking an AI agent to browse the web every time, you create small source-specific extractors.

For example:

- `competitor_blog_extract.py`
- `github_releases_extract.py`
- `security_advisories_extract.py`
- `newsletter_archive_extract.py`
- `custom_topic_extract.py`

Each extractor returns structured items. The sender script then combines them into a clean digest and sends it to Telegram or Slack.
