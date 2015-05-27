
-- phpMyAdmin SQL Dump
-- version 3.5.2.2
-- http://www.phpmyadmin.net
--
-- Client: localhost
-- Généré le: Mar 21 Avril 2015 à 19:11
-- Version du serveur: 5.1.66
-- Version de PHP: 5.2.17

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
--

-- --------------------------------------------------------

--
-- Structure de la table `Compteur`
--

CREATE TABLE IF NOT EXISTS `Compteur` (
  `Id_compteur` int(11) NOT NULL AUTO_INCREMENT,
  `Nom` varchar(20) COLLATE utf8_unicode_ci,
  `GPS_LAT` float,
  `GPS_LON` float,
  `Altitude` int,
  PRIMARY KEY (`Id_Compteur`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Structure de la table `Evenement`
--

CREATE TABLE IF NOT EXISTS `Evenement` (
  `Id_event` int(11) NOT NULL AUTO_INCREMENT,
  `Descriptif` varchar(1000) COLLATE utf8_unicode_ci NOT NULL,
  `Createur` int(11) NOT NULL,
  `Compteur` int(11),
  `Photo` varchar(20) COLLATE utf8_unicode_ci,
  PRIMARY KEY (`Id_event`),
  FOREIGN KEY (Createur) REFERENCES Exploitant (Id_exploitant),
  FOREIGN KEY (Compteur) REFERENCES Compteur (Id_compteur)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

CREATE TABLE IF NOT EXISTS `Exploitant` (
  `Id_exploitant` int(11) NOT NULL AUTO_INCREMENT,
  `Nom` varchar(60) COLLATE utf8_unicode_ci,
  `Mail` varchar(60) COLLATE utf8_unicode_ci,
  `Tel` varchar(20) COLLATE utf8_unicode_ci,
  `Login` varchar(256) COLLATE utf8_unicode_ci NOT NULL,
  `Password` varchar(256) COLLATE utf8_unicode_ci NOT NULL,
  `Salt` varchar(256) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`Id_exploitant`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=0 ;

-- --------------------------------------------------------

--
-- Structure de la table `Litige`
--

CREATE TABLE IF NOT EXISTS `Litige` (
  `Id_litige` int(11) NOT NULL AUTO_INCREMENT,
  `Etat` tinyint(1) NOT NULL,
  `Id_releve_1` int(11) NOT NULL,
  `Id_releve_2` int(11) NOT NULL,
  PRIMARY KEY (`Id_litige`),
  FOREIGN KEY (Id_releve_1) REFERENCES Releve (Id_releve),
  FOREIGN KEY (Id_releve_2) REFERENCES Releve (Id_releve)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Structure de la table `Parcelle`
--

CREATE TABLE IF NOT EXISTS `Parcelle` (
  `Id_parcelle` int(11) NOT NULL AUTO_INCREMENT,
  `Compteur` int(11),
  `Nom` varchar(60) COLLATE utf8_unicode_ci,
  `GPS_LAT` float,
  `GPS_LON` float,
  `Altitude` int,
  PRIMARY KEY (`Id_parcelle`),
  FOREIGN KEY (Compteur) REFERENCES Compteur (Id_compteur)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

-- Structure de la table `Propriete`

CREATE TABLE IF NOT EXISTS `Propriete` (
  `Id_propriete` int(11) NOT NULL AUTO_INCREMENT,
  `Id_parcelle` int(11) NOT NULL,
  `Id_exploitant` int(11),
  `date_debut` datetime,
  `date_fin` datetime,
  PRIMARY KEY (`Id_propriete`),
  FOREIGN KEY (Id_parcelle) REFERENCES Parcelle (Id_parcelle),
  FOREIGN KEY (Id_exploitant) REFERENCES Exploitant (Id_exploitant)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Structure de la table `Releve`
-- Exploitant : celui qui a consomme l.eau. L.administrateur peut entrer un releve au nom de n.importe qui.

CREATE TABLE IF NOT EXISTS `Releve` (
  `Id_releve` int(11) NOT NULL AUTO_INCREMENT,
  `Compteur` int(11) NOT NULL,
  `Exploitant` int(11) NOT NULL,
  `Index_début` int(11) NOT NULL,
  `Index_fin` int(11) NOT NULL,
  `Date` timestamp NOT NULL,
  
  PRIMARY KEY (`Id_releve`),
  FOREIGN KEY (Compteur) REFERENCES Compteur (Id_compteur)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
