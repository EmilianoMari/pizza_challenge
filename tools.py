from cat.mad_hatter.decorators import tool
import json
from .pizza import PizzaOrder


p = PizzaOrder()


@tool()
def book_pizza(tool_input, cat):
    """
    Usa questo tool se il messaggio è riferito all'ordine di una pizza. 
    Usa questo tool per prendere ordinazioni di pizze. Le infomazioni riguardano il tipo di pizza, l'indirizzo a cui portarla e
    il numero di telefono a del cliente che sta ordinando la pizza 

    tool_input è un dizionario che può contenere le seguenti chiavi:
    - pizza_type
    - address
    - floor
    - phone
    - delivery_time
    il valore in corrispondenza delle chiavi viene associato in solo base a quello che dice l'utente.
    """
    print("\n")
    print("TOOL-" * 20)

    print(tool_input)
    try:
        tool_input = tool_input.replace("'", '"', 10)
        dict_tool_input = json.loads(tool_input)
    except Exception as e:
        print(e)
        return "Perdonami ma non ho capito, puoi ripetere?"
        
    extra_error_message = ""
    for key in dict_tool_input:
        if cat.working_memory["recall_query"].lower() is not None and dict_tool_input[key].lower() in cat.working_memory["recall_query"].lower():
            if key == "pizza_type" and dict_tool_input[key].lower() not in ["margherita", "boscaiola", "capricciosa"]:
                extra_error_message = "Il tipo di pizza che hai chiesto non è disponibile"
                continue
            p.add_property(key, dict_tool_input[key])

    print("*" * 60)
    print(p.get_dict_raw())
    print("*" * 60)

    missing_info = p.check_values()
    if len(missing_info) > 0:
        return "Mancano queste informazioni: %s chiedile al cliente nei prossimi messaggi. %s" % (missing_info, extra_error_message)
    return "Ordine ricevuto!, ecco il resoconto: %s" % p.get_dict()


''' 
@tool
def recap_pizza_order(tool_input, cat):
    """
    Ritorna le informazioni inerenti all'ordine della pizza in corso. 
    Usa questo tool solo quando il cliente chiede un resoconto dell'ordine.
    """
    
    return cat.llm(
        """
        Ecco una lisa delle infomrazioni inserenti all'ordine di una pizza %s. 
        Le informazioni possono essere:
        - pizza_type
        - address
        - floor
        - phone
        - delivery_time
        - drink
        Alcune informazioni potrebbero essere mancanti e quindi non vanno incluse nel messaggio.
        Prepara un messaggio per il cliente con queste informazioni contenente una lista puntata con tutte le informazioni
        """ % p.get_dict()
    )
'''