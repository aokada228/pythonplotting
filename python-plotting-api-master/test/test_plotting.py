from python_plotting_api.plotting import get_breast_cancer_df, get_correlation_matrix_as_bytes, get_pair_plot_as_bytes


def test_get_data():
    df, features_names = get_breast_cancer_df()
    assert len(features_names) == 30
    assert len(list(df.columns)) == 32


def test_get_correlation_plot():
    df, features_names = get_breast_cancer_df()
    bytes_object = get_correlation_matrix_as_bytes(df[0:100], features_names)
    assert not bytes_object.closed


def test_get_pair_plot():
    cols = ['worst concave points', 'mean concavity',
            'worst perimeter', 'worst radius',
            'worst area']
    df, features_names = get_breast_cancer_df()
    bytes_object = get_pair_plot_as_bytes(df[0:1000],cols)
    assert not bytes_object.closed
