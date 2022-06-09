"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Scikit Jade."""


if __name__ == "__main__":
    main(prog_name="scikit-jade")  # pragma: no cover
