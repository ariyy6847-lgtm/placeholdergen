"""PlaceholderGen: Creates placeholder image files at any size and color."""

__version__ = "1.0.0"

from .core import run
from .cli import main

__all__ = ["main", "run", "__version__"]