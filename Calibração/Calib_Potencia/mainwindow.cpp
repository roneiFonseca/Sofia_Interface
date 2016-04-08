#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    this->connect(this->ui->pushButton_menos, SIGNAL(clicked()), this,SLOT(on_pushButton_menos_clicked()));
    this->connect(this->ui->pushButton_mais, SIGNAL(clicked()), this,SLOT(on_pushButton_mais_clicked()));
    this->counter=0;
    this->ui->lcdNumber->display(counter);
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_pushButton_menos_clicked()
{
    counter--;
    this->ui->lcdNumber->display(counter);
}

void MainWindow::on_pushButton_mais_clicked()
{
    counter++;
    this->ui->lcdNumber->display(counter);
}
