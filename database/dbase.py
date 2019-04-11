from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table, DateTime
from sqlalchemy.orm import relationship

from conexao import connpostgres
from sqlalchemy.ext.declarative import declarative_base

conn = connpostgres.Conexao()

engine = conn.conectar()

Base = declarative_base()

# produto_pedido =Table('produto_pedido', Base.metadata,
#                       Column('produto_id', Integer, ForeignKey('produto.id')),
#                       Column('pedido_id', Integer, ForeignKey('pedido.id'))
#                       )

class Arquivo(Base):
    __tablename__ = 'earqmetadados'
    id = Column(Integer, primary_key=True)
    nome = Column(String(400), nullable=False)
    tipo = Column(String(5), nullable=False)
    tamanho = Column(Integer, nullable=False)
    dtcriacao = Column(DateTime, nullable=True)
    dtatualizacao = Column(DateTime, nullable=True)

    # pedidos = relationship('Pedido', back_populates="cliente", cascade="delete")

    """ Retorna Instancia do objeto Arquivo """
    def __repr__(self):
        return "%s ('%s', '%s')" % (self.id, self.nome, self.tipo,self.tamanho, self.dtatualizacao, self.dtcriacao)

# class Pedido(Base):
#     __tablename__ = 'pedido'
#     id = Column(Integer, primary_key=True)
#
#     cliente_id = Column(Integer, ForeignKey('cliente.id'), nullable=False)
#     cliente = relationship("Cliente", back_populates='pedidos')
#
#     produtos = relationship("Produto",secondary="produto_pedido", back_populates="pedido")
#
#     def __repr__(self):
#         return "%s" % (self.id)

# class Produto(Base):
#     __tablename__ = 'produto'
#     id = Column(Integer, primary_key=True)
#     descricao = Column(String(40), nullable=False)
#     valor = Column(Float, nullable=False)
#
#     pedido = relationship("Pedido", secondary="produto_pedido", back_populates="produtos")
#
#     def __repr__(self):
#         return "Produto %s %s %s" % (self.id, self.descricao, self.valor)

Base.metadata.create_all(engine)
