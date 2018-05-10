from prompt_toolkit.filters.cli import ViNavigationMode, ViSelectionMode, ViMode
from prompt_toolkit.filters import Always, IsReadOnly
from IPython import get_ipython
from prompt_toolkit.key_binding.bindings.vi import create_operator_decorator, create_text_object_decorator, TextObject
from prompt_toolkit.document import Document
from prompt_toolkit.buffer import ClipboardData
from prompt_toolkit.selection import SelectionType

ip = get_ipython()
registry = ip.pt_cli.application.key_bindings_registry

handle = registry.add_binding
text_object = create_text_object_decorator(registry)
operator = create_operator_decorator(registry)

navigation_mode = ViNavigationMode() & ViMode() & Always()
selection_mode = ViSelectionMode() & ViMode() & Always()

@handle('t', filter=selection_mode, eager=True)
def _____(event):
  event.current_buffer.cursor_up(count=event.arg)

@handle('h', filter=selection_mode, eager=True)
def _____(event):
  event.current_buffer.cursor_down(count=event.arg)

@text_object('d', eager=True)
def _____(event):
  return TextObject(event.current_buffer.document.get_cursor_left_position(count=event.arg))

@handle('h', filter=navigation_mode, eager=True)
def _____(event):
  event.current_buffer.auto_down(
    count=event.arg, go_to_start_of_line_if_history_changes=True)

@handle('t', filter=navigation_mode, eager=True)
def _____(event):
  event.current_buffer.auto_up(
    count=event.arg, go_to_start_of_line_if_history_changes=True)

@text_object('n', eager=True)
def _____(event):
  return TextObject(event.current_buffer.document.get_cursor_right_position(count=event.arg))

@handle('j', 'j', filter=navigation_mode, eager=True)
def _____(event):
  """
  Delete line. (Or the following 'n' lines.)
  """
  buffer = event.current_buffer

  # Split string in before/deleted/after text.
  lines = buffer.document.lines

  before = '\n'.join(lines[:buffer.document.cursor_position_row])
  deleted = '\n'.join(lines[buffer.document.cursor_position_row:
                            buffer.document.cursor_position_row + event.arg])
  after = '\n'.join(lines[buffer.document.cursor_position_row + event.arg:])

  # Set new text.
  if before and after:
    before = before + '\n'

  # Set text and cursor position.
  buffer.document = Document(
    text=before + after,
    # Cursor At the start of the first 'after' line, after the leading whitespace.
    cursor_position = len(before) + len(after) - len(after.lstrip(' ')))

  # Set clipboard data
  event.cli.clipboard.set_data(ClipboardData(deleted, SelectionType.LINES))

@operator('j', filter=~IsReadOnly())
def delete_or_change_operator(event, text_object):
  clipboard_data = None
  buff = event.current_buffer

  if text_object:
    new_document, clipboard_data = text_object.cut(buff)
    buff.document = new_document
