
from gaphor.tests.testcase import TestCase
from gaphor.storage.storage import load


class PseudoFile(object):

    def __init__(self):
        self.data = ''

    def write(self, data):
        self.data += data


class ZaakspecificatieTestCase(TestCase):

    services = TestCase.services + ['crea-zaakspecificatie-export']

    def test_export(self):
        load('tests/cr2-superstate.gaphor', self.element_factory)
        zaakspec = self.get_service('crea-zaakspecificatie-export')

        pf = PseudoFile()
        zaakspec.export(pf)
        expected = ""
        assert pf.data == EXPECTED, '"""%s"""' % pf.data


EXPECTED = """<?xml version="1.0" encoding="utf-8"?>
<Zaakspecificatie>
<Toestandsverloop>
<Toestanden>
<Toestand Naam="`bekrachtigd">
<Transacties>
<Transactie>
<NaarToestand Naam="GeenNaam"/>
<Trigger Label=""/>
</Transactie>
</Transacties>
</Toestand>
<Toestand Naam="Beredeneerd">
<Transacties>
<Transactie>
<NaarToestand Naam="`bekrachtigd"/>
<Trigger Label=""/>
</Transactie>
<Transactie>
<NaarToestand Naam="Volledig"/>
<Trigger Label=""/>
</Transactie>
<Transactie>
<NaarToestand Naam="GeenNaam"/>
<Trigger Label=""/>
</Transactie>
</Transacties>
</Toestand>
<Toestand Naam="Volledig">
<Transacties>
<Transactie>
<NaarToestand Naam="`bekrachtigd"/>
<Trigger Zichtbaar="true" Commando="bekrachtigd" Label=""/>
</Transactie>
<Transactie>
<NaarToestand Naam="Onvolledig"/>
<Trigger Commando="speciaalVoorWim" Label=""/>
</Transactie>
</Transacties>
</Toestand>
<Toestand Naam="GeenNaam"/>
<Toestand Naam="GeenNaam"/>
<Toestand Naam="Aanvulling">
<Transacties>
<Transactie>
<NaarToestand Naam="Beredeneerd"/>
<Trigger Label=""/>
</Transactie>
</Transacties>
</Toestand>
<Toestand Naam="GeenNaam" StartToestand="true">
<Transacties>
<Transactie>
<NaarToestand Naam="Onvolledig"/>
<Trigger Zichtbaar="false" Commando="startZaak" Label="Aanmaken nieuwe zaak"/>
</Transactie>
</Transacties>
</Toestand>
<Toestand Naam="Onvolledig">
<Transacties>
<Transactie>
<NaarToestand Naam="Volledig"/>
<Trigger Label=""/>
</Transactie>
</Transacties>
</Toestand>
</Toestanden>
</Toestandsverloop>
</Zaakspecificatie>"""
# vim:sw=4:et:ai
