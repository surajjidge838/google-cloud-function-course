def hello_world(request):
    # request.arg can be dictionary and it might be empty
    request_args=request.args
    request_json=request.get_json(silent=True)

    if request_args and "fname" in request_args and "lname" in request_args:
        first_name=request_args["fname"]
        last_name=request_args["lname"]
    elif request_json and "fname" in request_json and "lname" in request_json:
        first_name = request_json[ "fname" ]
        last_name = request_json[ "lname" ]
    else:
        first_name="No"
        last_name="Fuss"
    return f"Hello {first_name} {last_name}..!"