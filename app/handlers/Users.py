from dataclasses import dataclass
from typing import Optional, Union
import msgpack


@dataclass
class User:
    id: int
    user_id: int
    link: Optional[str]
    first_name: str
    last_name: str
    goods: Union[bytes or dict]

    def __post_init__(self):
        self.goods_template = {'first_good': None,
                               'second_good': None,
                               'third_good': None
                               }
        if self.goods:
            self.goods = msgpack.loads(self.goods)

        if not self.goods:
            self.goods_msg = 'У вас нет записей!'
            self.goods = self.goods_template
        self.total_good = len(self.goods.keys())
        self.current_goods = len([i for i in self.goods.values() if i])

        # self.total_slots = 3
        # self.count_slots = self.total_slots
        # _empty_template = 'Не указан'
        #
        # if not self.first_good:
        #     self.count_slots -= 1
        #     self.first_good = _empty_template
        # if not self.second_good:
        #     self.count_slots -= 1
        #     self.second_good = _empty_template
        # if not self.third_good:
        #     self.count_slots -= 1
        #     self.third_good = _empty_template

    def dumps(self, d: dict) -> bytes:
        return msgpack.dumps(d)
