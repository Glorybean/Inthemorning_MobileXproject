from models.Inthemorning import InputModel, OutputModel
from utils.page import PageModel

def execute(
        page: PageModel,
        key: str,
        model: InputModel,
) -> OutputModel | None:
    return page.settingss.client.call(
        function=page.function,
        input=model,
        output_model=OutputModel,
    )