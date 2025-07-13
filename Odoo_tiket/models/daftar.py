from odoo import api, fields, models, _

class DaftarPesawat(models.Model):
    _name = "daftar.pesawat"
    _description = "Daftar Pesawat"


    # penumpang_id = fields.Many2one('tiket.pesawat', string="Nama", required=True)
    kelas_penerbangan=fields.Selection([
        ('economy', 'Economy'),
        ('business', 'Business'),
        ('first_class', 'First_Class')
    ], required=True, default='economy')    
            
    harga = fields.Float(string='Harga',  compute ='_compute_harga', store=True)
    
    @api.depends('kelas_penerbangan')
    def _compute_harga(self):
        for rec in self:
            if rec.kelas_penerbangan == 'economy' :
                rec.harga = 1000000
            elif rec.kelas_penerbangan == 'business' :
                rec.harga = 3000000
            elif rec.kelas_penerbangan == 'first_class' :
                rec.harga = 7000000
            else :
                rec.harga = 0

    kota_keberangkatan = fields.Selection([
            ('banyuwangi', 'Banyuwangi'),
            ('gresik', 'Gresik'),
            ('kediri', 'Kediri'),
            ('madura', 'Madura'),
            ('malang', 'Malang'),
            ('surabaya', 'Surabaya')
    ],  required=True)

    kota_tujuan = fields.Selection([
        ('banyuwangi', 'Banyuwangi'),
        ('gresik', 'Gresik'),
        ('kediri', 'Kediri'),
        ('madura', 'Madura'),
        ('malang', 'Malang'),
        ('surabaya', 'Surabaya')
    ],  required=True)  
    