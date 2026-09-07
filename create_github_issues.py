import re
import subprocess


# ============================================================
# SETTINGS
# ============================================================

MARKDOWN_FILE = "github_issues.md"

# Change this to your actual GitHub username/repository
REPOSITORY = "YOUR_GITHUB_USERNAME/Stay_Wyld_CI"

PROJECT_NAME = "Stay_Wyld_CI_PB"

# Set to False first to test what the script will create
CREATE_ISSUES = False


# ============================================================
# READ MARKDOWN FILE
# ============================================================

with open(MARKDOWN_FILE, "r", encoding="utf-8") as file:
    markdown = file.read()


# ============================================================
# FIND ALL USER STORIES
# ============================================================

pattern = r"^##\s+(US\d+):\s+(.+?)\s*\n(.*?)(?=^##\s+US\d+:|\Z)"

matches = re.findall(
    pattern,
    markdown,
    re.MULTILINE | re.DOTALL
)


print(f"Found {len(matches)} user stories.\n")


# ============================================================
# PROCESS EACH USER STORY
# ============================================================

for us_number, title, body in matches:

    title = title.strip()
    body = body.strip()

    # --------------------------------------------------------
    # Extract Priority
    # --------------------------------------------------------

    priority_match = re.search(
        r"^Priority:\s*(.+)$",
        body,
        re.MULTILINE
    )

    priority = (
        priority_match.group(1).strip()
        if priority_match
        else ""
    )

    # --------------------------------------------------------
    # Extract User Type
    # --------------------------------------------------------

    user_type_match = re.search(
        r"^User Type:\s*(.+)$",
        body,
        re.MULTILINE
    )

    user_type = (
        user_type_match.group(1).strip()
        if user_type_match
        else ""
    )

    # --------------------------------------------------------
    # Extract Labels
    # --------------------------------------------------------

    labels_match = re.search(
        r"^Labels:\s*(.+)$",
        body,
        re.MULTILINE
    )

    labels = []

    if labels_match:
        labels_text = labels_match.group(1).strip()

        labels = [
            label.strip()
            for label in labels_text.split(",")
            if label.strip()
        ]

    # --------------------------------------------------------
    # Remove metadata from issue body
    # --------------------------------------------------------

    issue_body = re.sub(
        r"^Priority:\s*.+$\n?",
        "",
        body,
        flags=re.MULTILINE
    )

    issue_body = re.sub(
        r"^User Type:\s*.+$\n?",
        "",
        issue_body,
        flags=re.MULTILINE
    )

    issue_body = re.sub(
        r"^Labels:\s*.+$\n?",
        "",
        issue_body,
        flags=re.MULTILINE
    )

    issue_body = issue_body.strip()

    # --------------------------------------------------------
    # Create GitHub issue title
    # --------------------------------------------------------

    full_title = f"{us_number}: {title}"

    print("=" * 60)
    print(f"Issue: {full_title}")
    print(f"Priority: {priority}")
    print(f"User Type: {user_type}")
    print(f"Labels: {labels}")
    print()
    print(issue_body[:300])
    print()

    # --------------------------------------------------------
    # DRY RUN
    # --------------------------------------------------------

    if not CREATE_ISSUES:
        print("DRY RUN - issue NOT created")
        continue

    # --------------------------------------------------------
    # Build GitHub CLI command
    # --------------------------------------------------------

    command = [
        "gh",
        "issue",
        "create",
        "--repo",
        REPOSITORY,
        "--title",
        full_title,
        "--body",
        issue_body,
    ]

    # Add labels
    for label in labels:
        command.extend([
            "--label",
            label
        ])

    # Add issue to GitHub Project
    command.extend([
        "--project",
        PROJECT_NAME
    ])

    # --------------------------------------------------------
    # Run GitHub CLI command
    # --------------------------------------------------------

    try:

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True
        )

        print("Created successfully:")
        print(result.stdout)

    except subprocess.CalledProcessError as error:

        print("ERROR creating issue:")
        print(error.stderr)


print("\nFinished.")