/********************************************************************************
** Form generated from reading UI file 'monidialog.ui'
**
** Created by: Qt User Interface Compiler version 5.5.1
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
    QLabel *label_2;
    QLabel *label;
    QLabel *label_12;
    QLabel *label_14;
    QLabel *label_15;
    QPushButton *pushButton_7;
    QLabel *label_17;
    QLabel *label_20;
    QLCDNumber *lcdNumber_7;
    QLabel *label_21;
    QPushButton *pushButton_8;
    QLCDNumber *lcdNumber_8;
    QLabel *label_22;
    QLCDNumber *lcdNumber_9;
    QLabel *label_23;
    QLabel *label_24;
    QLabel *label_25;
    QLCDNumber *lcdNumber_10;

    void setupUi(QDialog *moniDialog)
    {
        if (moniDialog->objectName().isEmpty())
            moniDialog->setObjectName(QStringLiteral("moniDialog"));
        moniDialog->resize(530, 465);
        moniDialog->setStyleSheet(QStringLiteral("background-color: rgb(255, 255, 255);"));
        label_2 = new QLabel(moniDialog);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setGeometry(QRect(90, 130, 441, 71));
        label_2->setStyleSheet(QStringLiteral("font: 22pt \"Times New Roman\";"));
        label_2->setAlignment(Qt::AlignCenter);
        label = new QLabel(moniDialog);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(0, 0, 681, 111));
        label->setPixmap(QPixmap(QString::fromUtf8("../imagens/logo.png")));
        label_12 = new QLabel(moniDialog);
        label_12->setObjectName(QStringLiteral("label_12"));
        label_12->setGeometry(QRect(400, 320, 91, 21));
        label_12->setStyleSheet(QStringLiteral("font: 16pt \"Times New Roman\";"));
        label_12->setAlignment(Qt::AlignCenter);
        label_14 = new QLabel(moniDialog);
        label_14->setObjectName(QStringLiteral("label_14"));
        label_14->setGeometry(QRect(400, 350, 47, 13));
        label_14->setStyleSheet(QStringLiteral("font: 75 12pt \"Times New Roman\";"));
        label_15 = new QLabel(moniDialog);
        label_15->setObjectName(QStringLiteral("label_15"));
        label_15->setGeometry(QRect(20, 390, 381, 16));
        pushButton_7 = new QPushButton(moniDialog);
        pushButton_7->setObjectName(QStringLiteral("pushButton_7"));
        pushButton_7->setGeometry(QRect(150, 430, 141, 21));
        label_17 = new QLabel(moniDialog);
        label_17->setObjectName(QStringLiteral("label_17"));
        label_17->setGeometry(QRect(410, 220, 111, 21));
        label_17->setStyleSheet(QStringLiteral("font: 16pt \"Times New Roman\";"));
        label_17->setAlignment(Qt::AlignCenter);
        label_20 = new QLabel(moniDialog);
        label_20->setObjectName(QStringLiteral("label_20"));
        label_20->setGeometry(QRect(400, 250, 47, 13));
        label_20->setStyleSheet(QStringLiteral("font: 75 12pt \"Times New Roman\";"));
        lcdNumber_7 = new QLCDNumber(moniDialog);
        lcdNumber_7->setObjectName(QStringLiteral("lcdNumber_7"));
        lcdNumber_7->setGeometry(QRect(320, 310, 71, 51));
        label_21 = new QLabel(moniDialog);
        label_21->setObjectName(QStringLiteral("label_21"));
        label_21->setGeometry(QRect(60, 120, 441, 71));
        label_21->setStyleSheet(QStringLiteral("font: 22pt \"Times New Roman\";"));
        label_21->setAlignment(Qt::AlignCenter);
        pushButton_8 = new QPushButton(moniDialog);
        pushButton_8->setObjectName(QStringLiteral("pushButton_8"));
        pushButton_8->setGeometry(QRect(320, 430, 75, 23));
        lcdNumber_8 = new QLCDNumber(moniDialog);
        lcdNumber_8->setObjectName(QStringLiteral("lcdNumber_8"));
        lcdNumber_8->setGeometry(QRect(320, 210, 71, 51));
        label_22 = new QLabel(moniDialog);
        label_22->setObjectName(QStringLiteral("label_22"));
        label_22->setGeometry(QRect(110, 320, 111, 31));
        label_22->setStyleSheet(QStringLiteral("font: 16pt \"Times New Roman\";"));
        label_22->setAlignment(Qt::AlignCenter);
        lcdNumber_9 = new QLCDNumber(moniDialog);
        lcdNumber_9->setObjectName(QStringLiteral("lcdNumber_9"));
        lcdNumber_9->setGeometry(QRect(10, 310, 71, 51));
        label_23 = new QLabel(moniDialog);
        label_23->setObjectName(QStringLiteral("label_23"));
        label_23->setGeometry(QRect(90, 250, 47, 13));
        label_23->setStyleSheet(QStringLiteral("font: 75 12pt \"Times New Roman\";"));
        label_24 = new QLabel(moniDialog);
        label_24->setObjectName(QStringLiteral("label_24"));
        label_24->setGeometry(QRect(90, 350, 47, 13));
        label_24->setStyleSheet(QStringLiteral("font: 75 12pt \"Times New Roman\";"));
        label_25 = new QLabel(moniDialog);
        label_25->setObjectName(QStringLiteral("label_25"));
        label_25->setGeometry(QRect(100, 220, 91, 21));
        label_25->setStyleSheet(QStringLiteral("font: 16pt \"Times New Roman\";"));
        label_25->setAlignment(Qt::AlignCenter);
        lcdNumber_10 = new QLCDNumber(moniDialog);
        lcdNumber_10->setObjectName(QStringLiteral("lcdNumber_10"));
        lcdNumber_10->setGeometry(QRect(10, 210, 71, 51));

        retranslateUi(moniDialog);
        QObject::connect(pushButton_8, SIGNAL(clicked()), moniDialog, SLOT(close()));

        QMetaObject::connectSlotsByName(moniDialog);
    } // setupUi

    void retranslateUi(QDialog *moniDialog)
    {
        moniDialog->setWindowTitle(QApplication::translate("moniDialog", "Dialog", 0));
        label_2->setText(QApplication::translate("moniDialog", "TELA DE MONITORAMENTO", 0));
        label->setText(QString());
        label_12->setText(QApplication::translate("moniDialog", "Tempo", 0));
        label_14->setText(QApplication::translate("moniDialog", "min", 0));
        label_15->setText(QApplication::translate("moniDialog", "Status da Abla\303\247\303\243o: Iniciando/ Em andamento/ Finalizada ", 0));
        pushButton_7->setText(QApplication::translate("moniDialog", "CONFIGURA\303\207\303\225ES ", 0));
        label_17->setText(QApplication::translate("moniDialog", "Temperatura", 0));
        label_20->setText(QApplication::translate("moniDialog", "\302\272C", 0));
        label_21->setText(QApplication::translate("moniDialog", "TELA DE MONITORAMENTO", 0));
        pushButton_8->setText(QApplication::translate("moniDialog", "DESLIGAR", 0));
        label_22->setText(QApplication::translate("moniDialog", "Imped\303\242ncia", 0));
        label_23->setText(QApplication::translate("moniDialog", "W", 0));
        label_24->setText(QApplication::translate("moniDialog", "\316\251", 0));
        label_25->setText(QApplication::translate("moniDialog", "Pot\303\252ncia", 0));
    } // retranslateUi

};

namespace Ui {
    class moniDialog: public Ui_moniDialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MONIDIALOG_H
