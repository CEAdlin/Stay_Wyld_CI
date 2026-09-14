import re
import subprocess

# ============================================================
# SETTINGS
# ============================================================

MARKDOWN_FILE = "github_issues.md"

REPOSITORY = "CEAdlin/Stay_Wyld_CI"

CREATE_ISSUES = False


# ============================================================
# READ MARKDOWN FILE
# ============================================================

with open(MARKDOWN_FILE, "r", encoding="utf-8") as file:
    markdown = file.read()


# ============================================================
# FIND ALL USER STORIES
# ============================================================
# Expected markdown format:
#
# ## US01: Title of the user story
# Priority: *Must Have*
# User Type: *Visitor*
# Labels: *frontend, visitor*
#
# Body text here...

pattern = (
    r"^##\s+(US\d+):\s+(.+?)\n"      # US number + title
    r"([\s\S]*?)(?=^##\s+US\d+:|\Z)" # body until next USxx or end
)

matches = re.findall(pattern, markdown, re.MULTILINE)

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
        r"^Priority:\s*\*(.+?)\*",
        body,
        re.MULTILINE
    )
    priority = priority_match.group(1).strip() if priority_match else ""

    # --------------------------------------------------------
    # Extract User Type
    # --------------------------------------------------------

    user_type_match = re.search(
        r"^User Type:\s*\*(.+?)\*",
        body,
        re.MULTILINE
    )
    user_type = user_type_match.group(1).strip() if user_type_match else ""

    # --------------------------------------------------------
    # Extract Labels
    # --------------------------------------------------------

    labels_match = re.search(
        r"^Labels:\s*\*(.+?)\*",
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

    issue_body = re.sub(r"^Priority:.*$", "", body, flags=re.MULTILINE | re.IGNORECASE)
    issue_body = re.sub(r"^User Type:.*$", "", issue_body, flags=re.MULTILINE | re.IGNORECASE)
    issue_body = re.sub(r"^Labels:.*$", "", issue_body, flags=re.MULTILINE | re.IGNORECASE)
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
        "gh", "issue", "create",
        "--repo", REPOSITORY,
        "--title", full_title,
        "--body", issue_body,
    ]

    for label in labels:
        command.extend(["--label", label])

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

        issue_url = result.stdout.strip()

        print("Created successfully:")
        print(issue_url)

        # ----------------------------------------------------
        # Add the newly created issue to GitHub Project #4
        # ----------------------------------------------------

        project_command = [
            "gh", "project", "item-add",
            "--owner", "CEAdlin",
            "--project", "4",
            "--url", issue_url,
        ]

        project_result = subprocess.run(
            project_command,
            capture_output=True,
            text=True,
        )

        if project_result.returncode == 0:
            print("Added to project successfully.")
        else:
            print("Could not add to project:")
            print(project_result.stderr)

    except subprocess.CalledProcessError as error:
        print("ERROR creating issue:")
        print(error.stderr)

print("\nFinished.")
