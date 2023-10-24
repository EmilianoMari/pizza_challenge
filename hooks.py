from cat.mad_hatter.decorators import hook


@hook
def before_cat_reads_message(message_dict: dict, cat):
    print("\n")
    print("HOOK-" * 20)

    if "pizza" in message_dict["text"].lower():
        print("Pizza nel messaggio")
        return message_dict
    
    response = cat.llm("Se il messaggio è riferito all'ordine di una pizza rispondi con si, ecco il messaggio: %s" % message_dict["text"])
    if "si" == response.lower()[0:2]:
        return message_dict
    
    add_message = ""
    info_array = ["address", "floor", "phone", "delivery_time"]
    response = cat.llm(
        "Sapendo che con qeusta chat si sta ordinando una pizza, quale infomrazione sta passando il cliente tra queste proposte %s? rspondi solo con una o più chiavi fornite. ecco il messaggio: %s" 
        % (", ".join(info_array), message_dict["text"]))
    for info in info_array:
        if info in response:
            add_message += info + " " 
    print(add_message)

    message = "Questa è una chat per ordinare una pizza, il messaggio del cliente è: %s" % message_dict["text"]

    if add_message != "":
        message += " le infomrazioni che probabilmente sta trasmettendo relative all'ordine di consegna della pizza sono: %s" % add_message 

    message_dict["text"] = message
    return message_dict