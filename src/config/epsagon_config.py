import epsagon

epsagon.init(
    token='03b6d382-54b5-4cba-adc8-f4add446f50a',
    app_name='Epsagon Application',
    metadata_only=False,
)


@epsagon.python_wrapper
def initiate_epsagon():
    return "It worked!"
