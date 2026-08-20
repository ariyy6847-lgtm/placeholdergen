"""Minimal example for PlaceholderGen."""

from placeholdergen import placeholdergen


def main():
 runner = placeholdergen({"name": "PlaceholderGen", "dry_run": False})
 result = runner.execute()
 print(result)


if __name__ == "__main__":
 main()