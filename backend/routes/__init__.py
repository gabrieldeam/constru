from controllers.example_controller import ExampleResource

def initialize_routes(api):
    api.add_resource(ExampleResource, '/example')
