from .__version__ import __description__, __title__, __version__

try:
    from ._main import main
except ImportError:     # pragma: no cover
    def main() -> None:
        import sys
        sys.exit(1)
