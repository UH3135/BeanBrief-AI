import logging
import kagglehub
from typing import Any
from dotenv import load_dotenv
from kagglehub import KaggleDatasetAdapter

from django.core.management.base import BaseCommand
from beanbrief.models import Beans


load_dotenv()
logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Kaggle에서 커피 데이터를 가져와 데이터베이스에 저장합니다.'

    def handle(self, *args: Any, **options: Any) -> str | None:
        dataset = kagglehub.load_dataset(
            KaggleDatasetAdapter.HUGGING_FACE,
            "schmoyote/coffee-reviews-dataset",
            "coffee_analysis.csv",
        )

        for data in dataset:
            logger.info(data)
            Beans.objects.create(
                name=data['name'],
                roster=data['roaster'],
                roast=data['roast'],
                origin=data['origin_1'] + data['origin_2'],
                price=data['100g_USD'],
                rating=data['rating'],
                review=data['desc_1'],
            )
