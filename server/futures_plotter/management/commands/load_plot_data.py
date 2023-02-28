import pathlib
import pandas as pd
from django.core.management.base import BaseCommand

from futures_plotter.models import FuturesDay

class Command(BaseCommand):
    help = "Loads futures data from a spreadsheet."

    def add_arguments(self, parser):
        parser.add_argument(
            "--file",
            nargs="?",
            required=True,
            help="Path to spreadsheet file.",
        )

    def create_object(self, df_dict):
        return FuturesDay(
            Date=df_dict["Date"],
            Open=df_dict["Open"],
            High=df_dict["High"],
            Low=df_dict["Low"],
            Close=df_dict["Close*"],
            Adj_Close=df_dict["Adj Close**"],
            Volume=df_dict["Volume"],
        )

    def handle(self, *args, **kwargs):
        path = kwargs["file"]
        print(f"Loading data from {path}")

        fp = pathlib.Path(path)
        if not fp.exists():
            raise FileNotFoundError("Cannot load data.")
        if not fp.suffix == ".xlsx":
            raise RuntimeError(f"Unsupported file type: {fp.suffix}")

        df = pd.read_excel(fp)
        df = df.replace(to_replace="-", value=None)
        print(df)

        days = [self.create_object(d) for d in df.to_dict("records")]
        FuturesDay.objects.bulk_create(days)
        print(f"Successfully created {len(days)} rows.")
