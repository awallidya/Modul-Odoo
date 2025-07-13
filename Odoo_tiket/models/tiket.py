from odoo import api, fields, models, _
from odoo.exceptions import MissingError, UserError, ValidationError
from datetime import datetime

class TiketPesawat(models.Model):
    _name = "tiket.pesawat"
    _description = "pembelian tiket pesawat antar daerah/kota se-provinsi Jawa Timur"
    

    name = fields.Char(string= 'Nama', required=True)
    reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                            default=lambda self:_('New'))
    age = fields.Integer(string= 'Umur')
    gender = fields.Selection([
        ('male', 'Laki-laki'),
        ('female', 'Perempuan'), 
        ('other', 'Lainnya'),
    ],  required=True, default='male')


    kota_keberangkatan = fields.Selection([
        ('banyuwangi', 'Banyuwangi'),
        ('gresik', 'Gresik'),
        ('kediri', 'Kediri'),
        ('madura', 'Madura'),
        ('malang', 'Malang'),
        ('surabaya', 'Surabaya')
    ], related='kelas_penerbangan_id.kota_keberangkatan',required=True)

    kota_tujuan = fields.Selection([
        ('banyuwangi', 'Banyuwangi'),
        ('gresik', 'Gresik'),
        ('kediri', 'Kediri'),
        ('madura', 'Madura'),
        ('malang', 'Malang'),
        ('surabaya', 'Surabaya')
    ],related='kelas_penerbangan_id.kota_tujuan',required=True)  

    
    
    # @api.onchange('kota_keberangkatan','kota_tujuan')
    # def _onchange_kota_keberangkatan(self) :
    #     if self.kota_keberangkatan == self.kota_tujuan :
    #         raise UserError("Kota keberangkatan dan kota tujuan anda sama")
        

    # # kelas_penerbangan = fields.Selection([
    # #     ('economy', 'Economy'),
    # #     ('business', 'Business'),
    # #     ('first_class', 'First_Class')
    # ], required=True, default='economy')  
    kursi = fields.Selection([
        ('a1', 'A1'),
        ('a2', 'A2'),
        ('a3', 'A3'),
        ('a4', 'A4'),
        ('a5', 'A5'),
        ('b1', 'B1'),
        ('b2', 'B2'),
        ('b3', 'B3'),
        ('b4', 'B4'),
        ('b5', 'B5')
    ],  required=True, default='a1')
    note = fields.Text(string='Catatan')
    # maskapai=fields.Text(string='Maskapai')
    # maskapai = fields.Text(string='Maskapaipenumpang_id = fields.Many2one('daftar.pesawat', string="Nama", required=True)
    # kelas_penerbangan=fields.Selection([
    #     ('economy', 'Economy'),
    #     ('business', 'Business'),
    #     ('first_class', 'First_Class')
    # ],related='penumpang_id.kelas_penerbangan', required=True, default='economy')  


    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                              ('done', 'Done'), ('cancel', 'Canceled')], default='draft', string="Status")
    @api.model
    def create(self, vals):
        if vals.get('note'):
           vals['note'] = 'New Ticket'
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('tiket.pesawat') or _('New')
        res = super(TiketPesawat, self).create(vals)
        return res
    
    tanggal = fields.Date(string='Tanggal')

    # def create(self, values):
    #     res = super(tanggal, self).create(values)
    #     for rec in res:
    #         tanggal_pembelian = rec.tanggal
    #         tanggal_sekarang = date.today()
    #         if tanggal_pembelian < tanggal_sekarang :
    #             raise ValidationError(_("Tanggal yang anda pilih telah berlalu"))

    @api.model_create_multi
    def _check_tanggal(self, vals_list) :
        for vals in vals_list :
            if not vals.get('tanggal'):
                raise ValidationError(_("Tanggal yang anda pilih sudah berlalu"))
            res = super(TiketPesawat, self).create(vals_list)
            return res

            
    # harga = fields.Float(string='Harga', related='penumpang_id.harga',compute ='_compute_harga', store=True)
    
    # @api.depends('kelas_penerbangan')
    # def _compute_harga(self):
    #     for rec in self:
    #         if rec.kelas_penerbangan == 'economy' :
    #             rec.harga = 1000000
    #         elif rec.kelas_penerbangan == 'business' :
    #             rec.harga = 3000000
    #         elif rec.kelas_penerbangan == 'first_class' :
    #             rec.harga = 7000000
    #         else :
    #             rec.harga = 0
    
    kelas_penerbangan_id= fields.Many2one('daftar.pesawat', string="Tujuan", required=True)
    harga = fields.Float(string='Harga', related='kelas_penerbangan_id.harga',compute ='_compute_harga', store=True)
    
    image=fields.Binary(string="Penumpang Image")

   

    