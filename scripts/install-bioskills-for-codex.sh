#!/usr/bin/env bash

set -euo pipefail

REPO_URL="https://github.com/GPTomics/bioSkills.git"
RELEASE_TAG="3.0"
EXPECTED_COMMIT="fae219d8cacb7be84b96b3a99122556c1a42a47b"
CACHE_DIR="${HOME}/.cache/codex-bioskills/repo"

print_usage() {
  cat <<'EOF'
Usage: install-bioskills-for-codex.sh [BIOskills installer options]

Wrapper around the upstream bioSkills Codex installer.

Examples:
  bash scripts/install-bioskills-for-codex.sh
  bash scripts/install-bioskills-for-codex.sh --categories "single-cell,variant-calling"
  bash scripts/install-bioskills-for-codex.sh --project
  bash scripts/install-bioskills-for-codex.sh --validate
  bash scripts/install-bioskills-for-codex.sh --update
  bash scripts/install-bioskills-for-codex.sh --uninstall

Environment:
  BIOskills_CACHE_DIR   Override the local cache directory
EOF
}

verify_commit() {
  local repo_dir="$1"
  local actual_commit
  actual_commit="$(git -C "$repo_dir" rev-parse HEAD 2>/dev/null || true)"
  [[ "$actual_commit" == "$EXPECTED_COMMIT" ]]
}

ensure_repo() {
  local repo_dir="${BIOskills_CACHE_DIR:-$CACHE_DIR}"

  if [[ -d "$repo_dir/.git" ]] && verify_commit "$repo_dir"; then
    printf 'Using cached bioSkills repo: %s\n' "$repo_dir" >&2
    printf '%s\n' "$repo_dir"
    return 0
  fi

  rm -rf "$repo_dir"
  mkdir -p "$(dirname "$repo_dir")"

  local tmpdir
  tmpdir="$(mktemp -d)"
  trap 'rm -rf "$tmpdir"' RETURN

  git clone --depth 1 --branch "$RELEASE_TAG" "$REPO_URL" "$tmpdir" >/dev/null 2>&1

  if ! verify_commit "$tmpdir"; then
    printf 'Repository integrity check failed for %s at tag %s\n' "$REPO_URL" "$RELEASE_TAG" >&2
    exit 1
  fi

  mv "$tmpdir" "$repo_dir"
  printf 'Cached bioSkills repo at: %s\n' "$repo_dir" >&2
  printf '%s\n' "$repo_dir"
}

main() {
  if [[ "${1:-}" == "--help" || "${1:-}" == "-h" ]]; then
    print_usage
    return 0
  fi

  if ! command -v git >/dev/null 2>&1; then
    printf 'git is required but was not found in PATH\n' >&2
    exit 1
  fi

  local repo_dir
  repo_dir="$(ensure_repo)"

  if [[ ! -f "$repo_dir/install-codex.sh" ]]; then
    printf 'Upstream install-codex.sh not found in %s\n' "$repo_dir" >&2
    exit 1
  fi

  bash "$repo_dir/install-codex.sh" "$@"
}

main "$@"
