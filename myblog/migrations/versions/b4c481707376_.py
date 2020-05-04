"""empty message

Revision ID: b4c481707376
Revises: fcec9e4443ca
Create Date: 2020-05-03 11:38:16.588402

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b4c481707376'
down_revision = 'fcec9e4443ca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('featured_article',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('article_title', sa.String(length=50), nullable=False),
    sa.Column('article_id', sa.Integer(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['article_id'], ['article.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('article', 'author_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('article', 'category_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('article', 'category_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('article', 'author_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.drop_table('featured_article')
    # ### end Alembic commands ###
