from typing import List, Dict, Union

class DetailedStatistics:
    def __init__(self, day:str, agency:int) -> None:
        self.day = day
        self.agency = agency

    def run_statistics(self, customers_served:List[str]) -> Dict:
        statistic:Dict[str, Union[List[str], str, int]] = {}

        statistic['day'] = self.day
        statistic['agency'] = self.agency
        statistic['customers_served'] = customers_served
        statistic['customers_served_count'] = len(customers_served)
        return statistic
