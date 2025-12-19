# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["BetaSearchLabelsResponse", "Result", "ResultLabel"]


class ResultLabel(BaseModel):
    """A label search result.

    Includes the location, text content, value,
    and score.
    """

    for_: str = FieldInfo(alias="for")
    """Cell reference or range that contains the labelled data"""

    text: str
    """Text content of the label"""

    value: str
    """The labelled data value(s).

    If a range of data is labelled, this will be a stringified JSON array
    """

    score: Optional[float] = None
    """
    Relevance ranking of the workbook in relation to the search results (higher is
    better)
    """


class Result(BaseModel):
    """
    Contains a workbook that includes data labels that match the search
    query.
    """

    creator_id: str
    """UUID for the user that uploaded the workbook.

    This will always be the UUID of the account linked to the API key used in the
    request.
    """

    description: str
    """Generated description summarising the contents of the workbook"""

    filename: str
    """Original filename of the workbook"""

    labels: List[ResultLabel]
    """Array of labels within the workbook that match the search query"""

    latest_version: int
    """Most recent version number of the workbook"""

    thumbnail_url: str
    """Absolute URL for a thumbnail of the workbook's first sheet"""

    workbook_id: str
    """UUID for the workbook"""

    score: Optional[float] = None
    """
    Relevance ranking of the workbook in relation to the search results (higher is
    better)
    """


class BetaSearchLabelsResponse(BaseModel):
    """The results of a spreadsheet data label search."""

    results: List[Result]
