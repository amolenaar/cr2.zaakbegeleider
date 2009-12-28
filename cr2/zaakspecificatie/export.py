
from zope import interface
from gaphor.interfaces import IService, IActionProvider
from gaphor import UML
from gaphor.core import _, inject, action, build_action_group
from gaphor.misc.xmlwriter import XMLWriter

class ZaakspecificatieExportPlugin(object):

    interface.implements(IService, IActionProvider)

    gui_manager = inject('gui_manager')

    menu_xml = """
      <ui>
        <menubar name="mainwindow">
          <menu action="file">
            <menu action="file-export">
              <menuitem action="zaakspecificatie-export" />
            </menu>
          </menu>
        </menubar>
      </ui>
    """

    element_factory = inject('element_factory')

    def __init__(self):
        self.action_group = build_action_group(self)

    def init(self, app):
        self._app = app
        log.info('Hello world plugin initialized')

    def shutdown(self):
        pass

    @action(name='zaakspecificatie-export', label=_('Zaakspecificatie XML'),
            tooltip=_('CR2 Zaakspecificatie XML'))
    def export_action(self):
        pass

    def export(self, filename):
        writer = XMLWriter(filename, 'utf-8')
        writer.startDocument()
        writer.startElement('Zaakspecificatie', {})
        # TODO: Header stuff
        writer.startElement('Toestandsverloop', {})
        self._export_toestanden(writer)
        writer.endElement('Toestandsverloop')
        writer.endElement('Zaakspecificatie')
        writer.endDocument()

    def _export_toestanden(self, writer):
        vertices = self.element_factory.select(lambda e: e.isKindOf(UML.Vertex))
        if not vertices:
            return

        writer.startElement('Toestanden', {})
        for toestand in vertices:
            attrs = { 'Naam': toestand.name or 'GeenNaam' }
            if toestand.isKindOf(UML.Pseudostate) and toestand.kind == 'initial':
                attrs['StartToestand'] = 'true'
            writer.startElement('Toestand', attrs)
            self._export_transacties(toestand, writer)
            writer.endElement('Toestand')
        writer.endElement('Toestanden')

    def _export_transacties(self, vertex, writer):
        if not vertex.outgoing:
            return
        writer.startElement('Transacties', {})
        for transactie in vertex.outgoing:
            writer.startElement('Transactie', {})
            writer.startElement('NaarToestand', { 'Naam': transactie.target.name or 'GeenNaam' })
            writer.endElement('NaarToestand')
            attrs = { 'Label': transactie.name or '' }
            for slot in transactie.appliedStereotype[:].slot:
                attrs[slot.definingFeature.name.title()] = slot.value[0].value
            writer.startElement('Trigger', attrs)
            writer.endElement('Trigger')
            writer.endElement('Transactie')
        writer.endElement('Transacties')


# vim: sw=4:et:ai
