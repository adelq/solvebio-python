from solvebio.resource import Depository

from .helper import SolveBioTestCase


class DepositoryTests(SolveBioTestCase):
    """
    Test Depository.
    """

    def test_depositories(self):
        # TODO: use TEST_DATASET_NAME.split('/')[0]
        depos = Depository.all()
        depo = depos.data[0]
        self.assertTrue('id' in depo,
                        'Should be able to get id in depository')

        depo2 = Depository.retrieve(depo.id)
        self.assertEqual(depo, depo2,
                         "Retrieving dataset id {0} found by all()"
                         .format(depo.id))

        check_fields = set(['class_name', 'created_at',
                            'description', 'external_resources',
                            'full_name', 'id',
                            'is_private', 'is_restricted',
                            'latest_version',
                            'latest_version_id',
                            'name', 'title', 'updated_at',
                            'url', 'versions_count', 'versions_url'])

        self.assertSetEqual(set(depo), check_fields)
        expected_start = """
|         Fields | Data                                                        |
|----------------+-------------------------------------------------------------|
|    description |
"""[1:-2]  # noqa

        self.assertTrue(repr(depo).startswith(expected_start),
                        'depository tabulate')
