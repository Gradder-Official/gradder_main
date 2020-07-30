from typing import List, Dict

def response(flashes: List[str], forms: Dict, **kwargs) -> dict:
    """Response factory for JSON backend

    Parameters
    ----------
    flashes : list
        The flashes on the page, used to replace flask's :func:`~Flash.flash` function
    forms : dict
        The forms to display on the page.

    Returns
    -------
    dict
        The response ready to send
    """
    return {
        'flashes': flashes,
        forms: forms,
        **kwargs
    }


def error(message: str, flash: bool = True) -> dict:
    """Error factory, wraps :func:`response`

    Parameters
    ----------
    message : str
        The error message
    flash : bool, optional
        Whether to display the error message as a flash, by default True

    Returns
    -------
    dict
        The response ready to send
    """
    flashes = []
    if flash:
        flashes.append(message)
    return response(flashes, error=message)

