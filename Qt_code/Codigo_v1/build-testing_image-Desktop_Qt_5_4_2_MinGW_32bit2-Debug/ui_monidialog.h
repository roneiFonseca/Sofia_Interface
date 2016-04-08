/********************************************************************************
** Form generated from reading UI file 'monidialog.ui'
**
** Created by: Qt User Interface Compiler version 5.4.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MONIDIALOG_H
#define UI_MONIDIALOG_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QDialog>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLCDNumber>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>

QT_BEGIN_NAMESPACE

class Ui_moniDialog
{
public:
    QLabel *label_3;
    QPushButton *pushButton_6;
    QLCDNumber *lcdNumber;
    QLabel *label_2;
    QLabel *label_4;
    QPushButton *pushButton_5;
    QLabel *label;
    QLCDNumber *lcdNumber_2;
    QLCDNumber *lcdNumber_3;
    QLCDNumber *lcdNumber_4;
    QLabel *label_5;
    QLabel *label_6;
    QLabel *label_7;
    QLabel *label_8;
    QLabel *label_9;
    QLabel *label_10;
    QLabel *label_11;

    void setupUi(QDialog *moniDialog)
    {
        if (moniDialog->objectName().isEmpty())
            moniDialog->setObjectName(QStringLiteral("moniDialog"));
        moniDialog->resize(638, 475);
        moniDialog->setStyleSheet(QStringLiteral("background-color: rgb(255, 255, 255);"));
        label_3 = new QLabel(moniDialog);
        label_3->setObjectName(QStringLiteral("label_3"));
        label_3->setGeometry(QRect(120, 230, 91, 21));
        label_3->setStyleSheet(QStringLiteral("font: 16pt \"Times New Roman\";"));
        label_3->setAlignment(Qt::AlignCenter);
        pushButton_6 = new QPushButton(moniDialog);
        pushButton_6->setObjectName(QStringLiteral("pushButton_6"));
        pushButton_6->setGeometry(QRect(180, 440, 121, 21));
        lcdNumber = new QLCDNumber(moniDialog);
        lcdNumber->setObjectName(QStringLiteral("lcdNumber"));
        lcdNumber->setGeometry(QRect(20, 220, 71, 51));
        label_2 = new QLabel(moniDialog);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setGeometry(QRect(90, 130, 441, 71));
        label_2->setStyleSheet(QStringLiteral("font: 22pt \"Times New Roman\";"));
        label_2->setAlignment(Qt::AlignCenter);
        label_4 = new QLabel(moniDialog);
        label_4->setObjectName(QStringLiteral("label_4"));
        label_4->setGeometry(QRect(450, 230, 111, 21));
        label_4->setStyleSheet(QStringLiteral("font: 16pt \"Times New Roman\";"));
        label_4->setAlignment(Qt::AlignCenter);
        pushButton_5 = new QPushButton(moniDialog);
        pushButton_5->setObjectName(QStringLiteral("pushButton_5"));
        pushButton_5->setGeometry(QRect(350, 440, 75, 23));
        label = new QLabel(moniDialog);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(0, 0, 681, 111));
        label->setPixmap(QPixmap(QString::fromUtf8("../untitled/imagens/teste.JPG")));
        lcdNumber_2 = new QLCDNumber(moniDialog);
        lcdNumber_2->setObjectName(QStringLiteral("lcdNumber_2"));
        lcdNumber_2->setGeometry(QRect(350, 220, 71, 51));
        lcdNumber_3 = new QLCDNumber(moniDialog);
        lcdNumber_3->setObjectName(QStringLiteral("lcdNumber_3"));
        lcdNumber_3->setGeometry(QRect(350, 320, 71, 51));
        lcdNumber_4 = new QLCDNumber(moniDialog);
        lcdNumber_4->setObjectName(QStringLiteral("lcdNumber_4"));
        lcdNumber_4->setGeometry(QRect(20, 320, 71, 51));
        label_5 = new QLabel(moniDialog);
        label_5->setObjectName(QStringLiteral("label_5"));
        label_5->setGeometry(QRect(440, 330, 91, 21));
        label_5->setStyleSheet(QStringLiteral("font: 16pt \"Times New Roman\";"));
        label_5->setAlignment(Qt::AlignCenter);
        label_6 = new QLabel(moniDialog);
        label_6->setObjectName(QStringLiteral("label_6"));
        label_6->setGeometry(QRect(120, 330, 111, 31));
        label_6->setStyleSheet(QStringLiteral("font: 16pt \"Times New Roman\";"));
        label_6->setAlignment(Qt::AlignCenter);
        label_7 = new QLabel(moniDialog);
        label_7->setObjectName(QStringLiteral("label_7"));
        label_7->setGeometry(QRect(20, 400, 291, 20));
        label_8 = new QLabel(moniDialog);
        label_8->setObjectName(QStringLiteral("label_8"));
        label_8->setGeometry(QRect(100, 260, 47, 13));
        label_8->setStyleSheet(QStringLiteral("font: 75 12pt \"Times New Roman\";"));
        label_9 = new QLabel(moniDialog);
        label_9->setObjectName(QStringLiteral("label_9"));
        label_9->setGeometry(QRect(100, 360, 47, 13));
        label_9->setStyleSheet(QStringLiteral("font: 75 12pt \"Times New Roman\";"));
        label_10 = new QLabel(moniDialog);
        label_10->setObjectName(QStringLiteral("label_10"));
        label_10->setGeometry(QRect(430, 260, 47, 13));
        label_10->setStyleSheet(QStringLiteral("font: 75 12pt \"Times New Roman\";"));
        label_11 = new QLabel(moniDialog);
        label_11->setObjectName(QStringLiteral("label_11"));
        label_11->setGeometry(QRect(430, 360, 47, 13));
        label_11->setStyleSheet(QStringLiteral("font: 75 12pt \"Times New Roman\";"));

        retranslateUi(moniDialog);
        QObject::connect(pushButton_5, SIGNAL(clicked()), moniDialog, SLOT(close()));

        QMetaObject::connectSlotsByName(moniDialog);
    } // setupUi

    void retranslateUi(QDialog *moniDialog)
    {
        moniDialog->setWindowTitle(QApplication::translate("moniDialog", "Dialog", 0));
        label_3->setText(QApplication::translate("moniDialog", "Pot\303\252ncia", 0));
        pushButton_6->setText(QApplication::translate("moniDialog", "CONFIGURA\303\207\303\225ES ", 0));
        label_2->setText(QApplication::translate("moniDialog", "TELA DE MONITORAMENTO", 0));
        label_4->setText(QApplication::translate("moniDialog", "Temperatura", 0));
        pushButton_5->setText(QApplication::translate("moniDialog", "DESLIGAR", 0));
        label->setText(QString());
        label_5->setText(QApplication::translate("moniDialog", "Tempo", 0));
        label_6->setText(QApplication::translate("moniDialog", "Imped\303\242ncia", 0));
        label_7->setText(QApplication::translate("moniDialog", "Status da Abla\303\247\303\243o: Iniciando/ Em andamento/ Finalizada ", 0));
        label_8->setText(QApplication::translate("moniDialog", "W", 0));
        label_9->setText(QApplication::translate("moniDialog", "\316\251", 0));
        label_10->setText(QApplication::translate("moniDialog", "\302\272C", 0));
        label_11->setText(QApplication::translate("moniDialog", "min", 0));
    } // retranslateUi

};

namespace Ui {
    class moniDialog: public Ui_moniDialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MONIDIALOG_H
