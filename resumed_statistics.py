from typing import List, Dict, Union

class ResumedStatistics:
    def __init__(self, day:str, agency:int) -> None:
        self.day = day
        self.agency = agency

    def run_statistics(self, customers_served:List[str]) -> Dict:
        statistic:Dict[str, Union[List[str], str, int]] = {}
        statistic[f'{self.agency}-{self.day}'] = len(customers_served)
        return statistic
