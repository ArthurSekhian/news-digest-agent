# Quick Start

This guide is for users who cloned this repository.

Run all commands from the repository root folder.

## 1. Test the example extractor

```bash
python3 extractors/examples/custom_topic_extract.py 2026-05-25 2026-05-31 --included-only
```

This should print example JSON with one candidate item.

## 2. Test the digest sender

```bash
python3 sender/send_digest.py
```

This should print a sample digest in Terminal.

## 3. Create your own extractor

Copy the example extractor:

```bash
cp extractors/examples/custom_topic_extract.py extractors/examples/competitor_blog_extract.py
```

Rename it based on your topic.

Examples:

```text
competitor_blog_extract.py
github_releases_extract.py
security_advisories_extract.py
newsletter_archive_extract.py
```

## 4. Edit your extractor

Update:

- source URL
- date parsing
- relevance rules
- category logic
- scoring logic

## 5. Add it to the sender

Open:

```text
sender/send_digest.py
```

Find:

```python
EXTRACTORS = [
    "extractors/examples/custom_topic_extract.py",
]
```

Add your new extractor:

```python
EXTRACTORS = [
    "extractors/examples/custom_topic_extract.py",
    "extractors/examples/competitor_blog_extract.py",
]
```

## 6. Configure delivery

By default, the sender prints the digest locally.

To send to Telegram or Slack, add your delivery logic in:

```text
sender/send_digest.py
```

## 7. Schedule it

Run manually:

```bash
python3 sender/send_digest.py
```

Or schedule it with cron, OpenClaw, GitHub Actions, or another scheduler.
