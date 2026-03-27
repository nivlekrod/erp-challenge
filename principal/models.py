from django.db import models

# Create your models here.
class Estado(models.Model):
    id = models.AutoField(primary_key=True, null=False)

    nome = models.CharField(
        db_column='tx_name',
        max_length=54,
        null=False,
        blank=False,
    )

    abreviacao = models.CharField(
        db_column='tx_abbreviation',
        max_length=2,
        null=False,
        blank=False,
    )

    ativo = models.BooleanField(
        db_column='cs_active',
        default=True,
        null=False,
        blank=False
    )

    criado_em = models.DateTimeField(
        auto_now_add=True,
        db_column='dt_created_at',
        null=False,
        blank=False
    )

    modificado_em = models.DateTimeField(
        auto_now=True,
        db_column='dt_modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'state'
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
        managed = True

    def __str__(self):
        return f"Estado {self.id} - {self.nome}"

class Cidade(models.Model):
    id = models.AutoField(primary_key=True, null=False)

    estado = models.ForeignKey(
        to='Estado',
        on_delete=models.DO_NOTHING,
        db_column='id_state',
        null=False,
        blank=False,
        related_name='cidades'
    )

    nome = models.CharField(
        db_column='tx_name',
        max_length=54,
        null=False,
        blank=False,
    )

    ativo = models.BooleanField(
        db_column='cs_active',
        default=True,
        null=False,
        blank=False
    )

    criado_em = models.DateTimeField(
        auto_now_add=True,
        db_column='dt_created_at',
        null=False,
        blank=False
    )

    modificado_em = models.DateTimeField(
        auto_now=True,
        db_column='dt_modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'city'
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
        managed = True
        unique_together = ('estado', 'nome')

    def __str__(self):
        return f"Cidade {self.id} - Estado: {self.estado.nome}"

class Zona(models.Model):
    id = models.AutoField(primary_key=True, null=False)

    nome = models.CharField(
        db_column='tx_name',
        max_length=54,
        null=False,
        blank=False,
    )

    ativo = models.BooleanField(
        db_column='cs_active',
        default=True,
        null=False,
        blank=False
    )

    criado_em = models.DateTimeField(
        auto_now_add=True,
        db_column='dt_created_at',
        null=False,
        blank=False
    )

    modificado_em = models.DateTimeField(
        auto_now=True,
        db_column='dt_modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'zone'
        verbose_name = 'Zona'
        verbose_name_plural = 'Zonas'
        managed = True

    def __str__(self):
        return f"Zona {self.id} {str(self.nome)}"

class Distrito(models.Model):
    id = models.AutoField(primary_key=True, null=False)

    zona = models.ForeignKey(
        to='Zona',
        on_delete=models.DO_NOTHING,
        db_column='id_zone',
        null=False,
        blank=False,
        related_name='distritos'
    )

    cidade = models.ForeignKey(
        to='Cidade',
        on_delete=models.DO_NOTHING,
        db_column='id_city',
        null=False,
        blank=False,
        related_name='distritos'
    )

    nome = models.CharField(
        db_column='tx_name',
        max_length=54,
        null=False,
        blank=False,
    )

    ativo = models.BooleanField(
        db_column='cs_active',
        default=True,
        null=False,
        blank=False
    )

    criado_em = models.DateTimeField(
        auto_now_add=True,
        db_column='dt_created_at',
        null=False,
        blank=False
    )

    modificado_em = models.DateTimeField(
        auto_now=True,
        db_column='dt_modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'district'
        verbose_name = 'Distrito'
        verbose_name_plural = 'Distritos'
        managed = True
        unique_together = ('zona', 'cidade')

    def __str__(self):
        return f"Distrito {self.id} - Cidade: {self.cidade.nome}"

class Filial(models.Model):
    id = models.AutoField(primary_key=True, null=False)

    distrito = models.ForeignKey(
        to='Distrito',
        on_delete=models.DO_NOTHING,
        db_column='id_district',
        null=False,
        blank=False,
        related_name='filiais'
    )

    nome = models.CharField(
        db_column='tx_name',
        max_length=54,
        null=False,
        blank=False
    )

    ativo = models.BooleanField(
        db_column='cs_active',
        default=True,
        null=False,
        blank=False
    )

    criado_em = models.DateTimeField(
        auto_now_add=True,
        db_column='dt_created_at',
        null=False,
        blank=False
    )

    modificado_em = models.DateTimeField(
        auto_now=True,
        db_column='dt_modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'branch_office'
        verbose_name = 'Filial'
        verbose_name_plural = 'Filiais'
        managed = True

    def __str__(self):
        return f"Filial {self.id} {self.nome}"

class EstadoCivil(models.Model):
    id = models.AutoField(primary_key=True, null=False)

    descricao = models.CharField(
        db_column='tx_description',
        max_length=54,
        null=False,
        blank=False
    )

    ativo = models.BooleanField(
        db_column='cs_active',
        default=True,
        null=False,
        blank=False
    )

    criado_em = models.DateTimeField(
        auto_now_add=True,
        db_column='dt_created_at',
        null=False,
        blank=False
    )

    modificado_em = models.DateTimeField(
        auto_now=True,
        db_column='dt_modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'marital_status'
        verbose_name = 'Estado Civil'
        verbose_name_plural = 'Estados Civis'
        managed = True

    def __str__(self):
        return f"Estado civil {self.id} {self.descricao}"

class Cliente(models.Model):
    id = models.AutoField(primary_key=True, null=False)

    estado_civil = models.ForeignKey(
        to='EstadoCivil',
        on_delete=models.DO_NOTHING,
        db_column='id_marital_status',
        null=False,
        blank=False,
        related_name='clientes'
    )

    distrito = models.ForeignKey(
        to='Distrito',
        on_delete=models.DO_NOTHING,
        db_column='id_district',
        null=False,
        blank=False,
        related_name='clientes'
    )

    nome = models.CharField(
        db_column='tx_name',
        max_length=54,
        null=False,
        blank=False
    )

    salario = models.DecimalField(
        db_column='nb_salary',
        max_digits=10,
        decimal_places=4,
        null=False,
        blank=False,
    )

    genero = models.CharField(
        db_column='cs_gender',
        max_length=1,
        null=False,
        blank=False
    )

    ativo = models.BooleanField(
        db_column='cs_active',
        default=True,
        null=False,
        blank=False
    )

    criado_em = models.DateTimeField(
        auto_now_add=True,
        db_column='dt_created_at',
        null=False,
        blank=False
    )

    modificado_em = models.DateTimeField(
        auto_now=True,
        db_column='dt_modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'customer'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        managed = True

    def __str__(self):
        return f"Cliente {self.id}: {self.nome}"

class Departamento(models.Model):
    id = models.AutoField(primary_key=True, null=False)

    nome = models.CharField(
        db_column='tx_name',
        max_length=54,
        null=False,
        blank=False
    )

    ativo = models.BooleanField(
        db_column='cs_active',
        default=True,
        null=False,
        blank=False
    )

    criado_em = models.DateTimeField(
        auto_now_add=True,
        db_column='dt_created_at',
        null=False,
        blank=False
    )

    modificado_em = models.DateTimeField(
        auto_now=True,
        db_column='dt_modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'department'
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        managed = True

    def __str__(self):
        return f"Departamento {self.id}"

class Funcionario(models.Model):
    id = models.AutoField(primary_key=True, null=False)

    gerente = models.ForeignKey(
        to='self',
        on_delete=models.SET_NULL,
        db_column='id_manager',
        null=True,
        blank=True,
        related_name='funcionarios'
    )

    departamento = models.ForeignKey(
        to='Departamento',
        on_delete=models.DO_NOTHING,
        db_column='id_department',
        null=False,
        blank=False,
        related_name='funcionarios'
    )

    estado_civil = models.ForeignKey(
        to='EstadoCivil',
        on_delete=models.DO_NOTHING,
        db_column='id_marital_status',
        null=False,
        blank=False,
        related_name='funcionarios'
    )

    nome = models.CharField(
        db_column='tx_name',
        max_length=54,
        null=False,
        blank=False
    )

    salario = models.DecimalField(
        db_column='nb_salary',
        max_digits=10,
        decimal_places=4,
        null=False,
        blank=False,
    )

    admissao = models.DateField(
        db_column='dt_adminission',
        null=False,
        blank=False
    )

    nascimento = models.DateField(
        db_column='dt_birth',
        null=False,
        blank=False
    )

    ativo = models.BooleanField(
        db_column='cs_active',
        default=True,
        null=False,
        blank=False
    )

    criado_em = models.DateTimeField(
        auto_now_add=True,
        db_column='dt_created_at',
        null=False,
        blank=False
    )

    modificado_em = models.DateTimeField(
        auto_now=True,
        db_column='dt_modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'employee'
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'
        managed = True

    def __str__(self):
        return f"Funcionario {self.nome}"

class Venda(models.Model):
    id = models.AutoField(primary_key=True, null=False)

    filial = models.ForeignKey(
        to='Filial',
        on_delete=models.DO_NOTHING,
        db_column='id_branch_office',
        null=False,
        blank=False,
        related_name='vendas'
    )

    funcionario = models.ForeignKey(
        to='Funcionario',
        on_delete=models.DO_NOTHING,
        db_column='id_employee',
        null=False,
        blank=False,
        related_name='vendas'
    )

    cliente = models.ForeignKey(
        to='Cliente',
        on_delete=models.DO_NOTHING,
        db_column='id_customer',
        null=False,
        blank=False,
        related_name='vendas'
    )

    vendido_em = models.DateTimeField(
        db_column='dt_sale',
        null=True,
        blank=True
    )

    ativo = models.BooleanField(
        db_column='cs_active',
        default=True,
        null=False,
        blank=False
    )

    criado_em = models.DateTimeField(
        auto_now_add=True,
        db_column='dt_created_at',
        null=False,
        blank=False
    )

    modificado_em = models.DateTimeField(
        auto_now=True,
        db_column='dt_modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'sale'
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'
        managed = True

    def __str__(self):
        return f"Venda {self.id} - Cliente: {self.cliente.nome}"

class FormaPagamento(models.Model):
    id = models.AutoField(primary_key=True, null=False)

    descricao = models.CharField(
        db_column='tx_description',
        max_length=54,
        null=False,
        blank=False
    )

    ativo = models.BooleanField(
        db_column='cs_active',
        default=True,
        null=False,
        blank=False
    )

    criado_em = models.DateTimeField(
        auto_now_add=True,
        db_column='dt_created_at',
        null=False,
        blank=False
    )

    modificado_em = models.DateTimeField(
        auto_now=True,
        db_column='dt_modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'means_payment'
        verbose_name = 'Forma de Pagamento'
        verbose_name_plural = 'Formas de Pagamento'
        managed = True

    def __str__(self):
        return f"Pagamento {self.id} {str(self.descricao)}"

class PagamentoVenda(models.Model):
    id = models.AutoField(primary_key=True, null=False)

    venda = models.ForeignKey(
        to='Venda',
        on_delete=models.DO_NOTHING,
        db_column='id_sale',
        null=False,
        blank=False,
        related_name='pagamentos_das_venda'
    )

    forma_pagamento = models.ForeignKey(
        to='FormaPagamento',
        on_delete=models.DO_NOTHING,
        db_column='id_means_payment',
        null=False,
        blank=False,
        related_name='pagamentos_das_vendas'
    )

    valor = models.DecimalField(
        db_column='nb_value',
        max_digits=10,
        decimal_places=4,
        null=False,
        blank=False,
    )

    ativo = models.BooleanField(
        db_column='cs_active',
        default=True,
        null=False,
        blank=False
    )

    criado_em = models.DateTimeField(
        auto_now_add=True,
        db_column='dt_created_at',
        null=False,
        blank=False
    )

    modificado_em = models.DateTimeField(
        auto_now=True,
        db_column='dt_modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'means_payment_sale'
        verbose_name = 'Pagamento da Venda'
        verbose_name_plural = 'Pagamentos das Vendas'
        managed = True

    def __str__(self):
        return f"Pagamento {self.id} {str(self.forma_pagamento)}"

class GrupoProduto(models.Model):
    id = models.AutoField(primary_key=True, null=False)

    descricao = models.CharField(
        db_column='tx_description',
        max_length=54,
        null=False,
        blank=False
    )

    percentual_comissao = models.DecimalField(
        db_column='nb_commission_percentage',
        max_digits=10,
        decimal_places=4,
        null=False,
        blank=False
    )

    percentual_ganho = models.DecimalField(
        db_column='nb_gain_percentage',
        max_digits=10,
        decimal_places=4,
        null=False,
        blank=False
    )

    ativo = models.BooleanField(
        db_column='cs_active',
        default=True,
        null=False,
        blank=False
    )

    criado_em = models.DateTimeField(
        auto_now_add=True,
        db_column='dt_created_at',
        null=False,
        blank=False
    )

    modificado_em = models.DateTimeField(
        auto_now=True,
        db_column='dt_modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'product_group'
        verbose_name = 'Grupo de Produto'
        verbose_name_plural = 'Grupos de Produtos'
        managed = True

    def __str__(self):
        return f"Grupo de Produto {self.id} {str(self.descricao)}"

class FornecedorProduto(models.Model):
    id = models.AutoField(primary_key=True, null=False)

    distrito = models.ForeignKey(
        to='Distrito',
        on_delete=models.DO_NOTHING,
        db_column='id_district',
        null=False,
        blank=False,
        related_name='fornecedor_produto'
    )

    nome = models.CharField(
        db_column='tx_name',
        max_length=54,
        null=False,
        blank=False
    )

    ativo = models.BooleanField(
        db_column='cs_active',
        default=True,
        null=False,
        blank=False
    )

    criado_em = models.DateTimeField(
        auto_now_add=True,
        db_column='dt_created_at',
        null=False,
        blank=False
    )

    modificado_em = models.DateTimeField(
        auto_now=True,
        db_column='dt_modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'supplier'
        verbose_name = 'Fornecedor de Produto'
        verbose_name_plural = 'Fornecedores de Produtos'
        managed = True

    def __str__(self):
        return f"Fornecedor de Produto {self.id} - {str(self.nome)} - {str(self.distrito)}"

class Produto(models.Model):
    id = models.AutoField(primary_key=True, null=False)

    grupo_de_produto = models.ForeignKey(
        to='GrupoProduto',
        on_delete=models.DO_NOTHING,
        db_column='id_product_group',
        null=False,
        blank=False,
        related_name='produtos'
    )

    fornecedor_produto = models.ForeignKey(
        to='FornecedorProduto',
        on_delete=models.DO_NOTHING,
        db_column='id_supplier',
        null=False,
        blank=False,
        related_name='produtos'
    )

    nome = models.CharField(
        db_column='tx_name',
        max_length=54,
        null=False,
        blank=False
    )

    preco_custo = models.DecimalField(
        db_column='nb_cost_price',
        max_digits=10,
        decimal_places=4,
        null=False,
        blank=False
    )

    preco_venda = models.DecimalField(
        db_column='nb_sale_price',
        max_digits=10,
        decimal_places=4,
        null=False,
        blank=False
    )

    ativo = models.BooleanField(
        db_column='cs_active',
        default=True,
        null=False,
        blank=False
    )

    criado_em = models.DateTimeField(
        auto_now_add=True,
        db_column='dt_created_at',
        null=False,
        blank=False
    )

    modificado_em = models.DateTimeField(
        auto_now=True,
        db_column='dt_modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'product'
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        managed = True

    def __str__(self):
        return f"Produto {self.id} - {str(self.nome)}"

class ItemVenda(models.Model):
    id = models.AutoField(primary_key=True, null=False)

    venda = models.ForeignKey(
        to='Venda',
        on_delete=models.DO_NOTHING,
        db_column='id_sale',
        null=False,
        blank=False,
        related_name='items_venda'
    )

    produto = models.ForeignKey(
        to='Produto',
        on_delete=models.DO_NOTHING,
        db_column='id_product',
        null=False,
        blank=False,
        related_name='items_venda'
    )

    quantidade = models.DecimalField(
        db_column='nb_quantity',
        max_digits=10,
        decimal_places=3,
        null=False,
        blank=False
    )

    preco_venda = models.DecimalField(
        db_column='nb_sale_price',
        max_digits=10,
        decimal_places=4,
        null=False,
        blank=False
    )

    subtotal = models.DecimalField(
        db_column='nb_subtotal',
        max_digits=10,
        decimal_places=4,
        null=False,
        blank=False
    )

    ativo = models.BooleanField(
        db_column='cs_active',
        default=True,
        null=False,
        blank=False
    )

    criado_em = models.DateTimeField(
        auto_now_add=True,
        db_column='dt_created_at',
        null=False,
        blank=False
    )

    modificado_em = models.DateTimeField(
        auto_now=True,
        db_column='dt_modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'sale_item'
        verbose_name = 'Item de Venda'
        verbose_name_plural = 'Itens de Vendas'
        managed = True

    def __str__(self):
        return f"Item de Venda {self.id} - {str(self.venda)}"