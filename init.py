from IPython.display import HTML


def scriptHTML():
    script = '''
        <script>
        
        function code_toggle(identifier) {
        
        code_cell = $( "span:contains(" + identifier + "):last" ).parentsUntil('div.cell').last().parent().next().children().first();
        
        if ($(code_cell).is(':visible')) {
        code_cell.hide();
        }
        else
        {
        code_cell.show();
        }
        
        }

        function hide_all() {
             $('div.input').hide();
        }

        $( document ).ready(hide_all);

        </script>
        '''
    
    return HTML(script)


def hide_code_message(identifier,message="Show/Hide Code"):
    form_start1 = ''' <form action=\"javascript:code_toggle('''
    identifier = "'" + identifier +  "'"
    form_start2 = ''')\"> <input type=\"submit\" value= '''
    form_end = '''></form>'''
    
    #print (form_start1 + identifier + form_start2 + '"' + message + '"' + form_end)
    return HTML(form_start1 + identifier + form_start2 + '"' + message + '"' + form_end)


def init_plotly():
    py.sign_in('cloaked', 'wiwoxbjrvr')