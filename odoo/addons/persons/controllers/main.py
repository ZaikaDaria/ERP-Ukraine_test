from odoo import http
from odoo.http import request

class PersonsController(http.Controller):
    @http.route('/persons', auth='public', website=True)
    def persons_list(self, **kwargs):
        persons = request.env['persons'].sudo().search([], order='id desc', limit=5)
        return request.render('your_module_name.persons_template', {'persons': persons})

    @http.route('/persons/add', auth='public', website=True, methods=['POST'], csrf=False)
    def add_person(self, **post):
        vals = {
            'first_name': post.get('first_name'),
            'last_name': post.get('last_name'),
            'birthday': post.get('birthday'),
            'sex': post.get('sex'),
            'company_id': request.env.user.company_id.id,
        }
        request.env['persons'].sudo().create(vals)
        return request.redirect('/persons')