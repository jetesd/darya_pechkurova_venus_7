import data
import create_order_request
import order_data_request


def get_user_body(first_name):
    current_body = data.order_body.copy()
    current_body["firstName"] = first_name
    return current_body
def test_create_new_order_and_get_it_by_track_number():
    user_body = get_user_body("Darya")
    create_order_response = create_order_request.post_new_order(user_body)
    track = create_order_response.json()["track"]
    order_get_response = order_data_request.get_order(track)
    assert order_get_response.status_code == 200