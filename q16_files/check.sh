set -e

ruff format
ruff check --fix
pytest
