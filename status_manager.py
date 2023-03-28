status = {
    "bonus_vacated": False,
    "corner_vacated": False,
    "bottom_search_vacated": False
}


def get_status(statusType: str = ""):
    if statusType == "all":
        return status["bonus_vacated"] and status["corner_vacated"] and status["bottom_search_vacated"]
    return status[statusType]


def update_status(statusType: str = ""):
    status[f"{statusType}_vacated"] = True
