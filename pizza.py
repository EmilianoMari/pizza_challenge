import uuid


def gen_piazza_dict():
    return {
        "id": uuid.uuid1(),
        "pizza_type": "",
        "address": "",
        "floor": "",
        "phone": "",
        "delivery_time": ""
    }


class PizzaOrder:
    def __init__(self) -> None:
        self.pizza_dict =  gen_piazza_dict()
    
    def get_dict_raw(self):
        return self.pizza_dict

    def get_dict(self):
        return ", ".join([f"{key}: {value}" for key, value in self.pizza_dict.items()])

    def reset_dict(self):
        self.pizza_dict = gen_piazza_dict()

    def add_property(self, property, value) -> None:
        self.pizza_dict[property] = value

    def check_values(self):
        missing_values = []
        for key in self.pizza_dict:
            if self.pizza_dict[key] == "":
               missing_values.append(key)
        return [] if len(missing_values) == 0 else ", ".join(missing_values)