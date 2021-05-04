from controllers import department_controller, employee_controller, employee_information_controller, \
    permission_controller, supervisor_controller, training_controller, tuition_controller


def route(app):
    department_controller.route(app)
    employee_controller.route(app)
    employee_information_controller.route(app)
    permission_controller.route(app)
    supervisor_controller.route(app)
    training_controller.route(app)
    tuition_controller.route(app)
