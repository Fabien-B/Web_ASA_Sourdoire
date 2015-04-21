
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
-- Base de données: `u696608455_bevep`
--

-- --------------------------------------------------------

--
-- Structure de la table `Borne`
--

CREATE TABLE IF NOT EXISTS `Borne` (
  `Id_Borne` int(11) NOT NULL AUTO_INCREMENT,
  `Nom` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `GPS_LAT` float NOT NULL,
  `GPS_LON` float NOT NULL,
  PRIMARY KEY (`Id_Borne`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Structure de la table `Evenement`
--

CREATE TABLE IF NOT EXISTS `Evenement` (
  `Id_event` int(11) NOT NULL AUTO_INCREMENT,
  `Descriptif` varchar(1000) COLLATE utf8_unicode_ci NOT NULL,
  `Createur` int(11) NOT NULL,
  `Photo_1` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `Photo_2` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`Id_event`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Structure de la table `Exploitant`
--

CREATE TABLE IF NOT EXISTS `Exploitant` (
  `Id_exploitant` int(11) NOT NULL AUTO_INCREMENT,
  `Nom` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `Prenom` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `Date_naiss` datetime NOT NULL,
  `Mail` varchar(60) COLLATE utf8_unicode_ci NOT NULL,
  `Tel` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`Id_exploitant`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Structure de la table `Litige`
--

CREATE TABLE IF NOT EXISTS `Litige` (
  `Id_litige` int(11) NOT NULL AUTO_INCREMENT,
  `Etat` tinyint(1) NOT NULL,
  `Id_releve_1` int(11) NOT NULL,
  `Id_releve_2` int(11) NOT NULL,
  PRIMARY KEY (`Id_litige`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Structure de la table `Parcelle`
--

CREATE TABLE IF NOT EXISTS `Parcelle` (
  `Id_parcelle` int(11) NOT NULL AUTO_INCREMENT,
  `Nom` varchar(60) COLLATE utf8_unicode_ci NOT NULL,
  `GPS_LAT` float NOT NULL,
  `GPS_LON` float NOT NULL,
  `Propiétaire` int(11) NOT NULL,
  `Borne` int(11) NOT NULL,
  PRIMARY KEY (`Id_parcelle`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Structure de la table `Propriete`
--

CREATE TABLE IF NOT EXISTS `Propriete` (
  `Id_parcelle` int(11) NOT NULL,
  `Id_exploitant` int(11) NOT NULL,
  `date_debut` datetime NOT NULL,
  `date_fin` datetime NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Structure de la table `Relevé`
--

CREATE TABLE IF NOT EXISTS `Relevé` (
  `Id_relevé` int(11) NOT NULL AUTO_INCREMENT,
  `Date` datetime NOT NULL,
  `Index_début` int(11) NOT NULL,
  `Index_fin` int(11) NOT NULL,
  `Créateur` int(11) NOT NULL,
  `Borne` int(11) NOT NULL,
  PRIMARY KEY (`Id_relevé`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
