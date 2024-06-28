from __future__ import annotations

import rich


def print_help() -> None:
    console = rich.console.Console()

    console.print("[bold]ftnx", justify="center")
    console.print()
    console.print("A next generation HTTP client.", justify="center")
    console.print()
    console.print(
        "Usage: [bold]ftnx[/bold] [red]OPT[/red] [cyan]--ARG[/cyan]", justify="left"
    )
    console.print()


def main() -> None:
    """
    A Fortanix DSM command line client.
    Creates and manages security objects within your cloud-based HSM.
    """