from ..agent import model
from src.model.structured_model_schema.title_generator_schema import Title
title_generator_model=model.with_structured_output(Title)