from cat.mad_hatter.decorators import hook


@hook
def before_cat_reads_message(message_dict: dict, cat):
    print("\n")
    print("HOOK-" * 20)

    if "pizza" in message_dict["text"].lower():
        return message_dict
    
    response = cat.llm("Se il messaggio è riferito all'ordine di una pizza rispondi con si, ecco il messaggio: %s" % message_dict["text"])
    print(response)
    if "si" == response.lower():
        return message_dict

    message = "Questa è una chat per ordinare una pizza, il messaggio del cliente è: %s" % message_dict["text"]
    message_dict["text"] = message
    return message_dict