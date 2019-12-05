from python_plotting_api.app import app

test_client = app.test_client()


def test_root():
    response = test_client.get('/')

    assert 200 == response.status_code


def test_get_correlation_matrix():
    response = test_client.get('/plots/breast_cancer_data/correlation_matrix')

    assert 200 == response.status_code
    assert 'image/png' == response.content_type


def test_get_pairplot_matrix():
    cols = ['worst concave points', 'mean concavity',
            'worst perimeter', 'worst radius',
            'worst area']

    query_string = ','.join(cols)
    response = test_client.get(f'/plots/breast_cancer_data/pairplot/features/{query_string}')

    assert 200 == response.status_code
    assert 'image/png' == response.content_type

    cols = ['worst concave points', 'mean concavity',
            'worst perimeter', 'worst radius',
            'worst area', 'wrong_feature']

    query_string = ','.join(cols)
    response = test_client.get(f'/plots/breast_cancer_data/pairplot/features/{query_string}')

    assert 400 == response.status_code

