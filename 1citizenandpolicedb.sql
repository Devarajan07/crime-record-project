-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 21, 2025 at 02:44 PM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `1citizenandpolicedb`
--

-- --------------------------------------------------------

--
-- Table structure for table `crimetb`
--

CREATE TABLE `crimetb` (
  `id` bigint(10) NOT NULL,
  `OfficerName` varchar(250) NOT NULL,
  `StationNo` varchar(250) NOT NULL,
  `Date` varchar(250) NOT NULL,
  `Applicant` varchar(250) NOT NULL,
  `ApAddress` varchar(500) NOT NULL,
  `Respondent` varchar(250) NOT NULL,
  `CaseInfo` varchar(500) NOT NULL,
  `Status` varchar(250) NOT NULL,
  `Info` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `crimetb`
--

INSERT INTO `crimetb` (`id`, `OfficerName`, `StationNo`, `Date`, `Applicant`, `ApAddress`, `Respondent`, `CaseInfo`, `Status`, `Info`, `UserName`) VALUES
(0, 'mark', '123', '2025-03-06', 'Jack', 'Trichy', 'Mark', 'null', 'Completed', 'nil', ''),
(0, 'mark', '123', '2025-03-07', 'Jack', 'Trichy', 'Jack', 'nul', 'Completed', 'nil', ''),
(0, 'mark', '1259', '2025-03-07', 'antony', 'Trichy', 'Mani', 'theft', 'Completed', 'nil', ''),
(0, 'mark', '123', '2025-03-21', 'Jack', 'Trichy', 'Mark', 'nil', 'Completed', 'nil', ''),
(0, 'mark', '123', '2025-03-21', 'Jack', 'nil', 'nil', 'nil', 'Completed', 'nil', 'mark');

-- --------------------------------------------------------

--
-- Table structure for table `evidancetb`
--

CREATE TABLE `evidancetb` (
  `id` bigint(10) NOT NULL,
  `OfficerName` varchar(250) NOT NULL,
  `StationNo` varchar(250) NOT NULL,
  `FIRNumber` varchar(250) NOT NULL,
  `Date` varchar(250) NOT NULL,
  `EvidenceName` varchar(250) NOT NULL,
  `location` varchar(500) NOT NULL,
  `info` varchar(250) NOT NULL,
  `Image` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `evidancetb`
--

INSERT INTO `evidancetb` (`id`, `OfficerName`, `StationNo`, `FIRNumber`, `Date`, `EvidenceName`, `location`, `info`, `Image`) VALUES
(0, 'jack', '1259', 'FIR145', '2025-03-06', 'Numberplate', 'Chennai', 'Car', '9818.png');

-- --------------------------------------------------------

--
-- Table structure for table `firtb`
--

CREATE TABLE `firtb` (
  `id` bigint(10) NOT NULL auto_increment,
  `OfficerName` varchar(250) NOT NULL,
  `StationNo` varchar(250) NOT NULL,
  `FIRNumber` varchar(250) NOT NULL,
  `Date` varchar(250) NOT NULL,
  `Applicant` varchar(250) NOT NULL,
  `ApAddress` varchar(500) NOT NULL,
  `Respondent` varchar(250) NOT NULL,
  `CaseInfo` varchar(500) NOT NULL,
  `Section` bigint(250) NOT NULL,
  `Hash1` varchar(250) NOT NULL,
  `Hash2` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `firtb`
--

INSERT INTO `firtb` (`id`, `OfficerName`, `StationNo`, `FIRNumber`, `Date`, `Applicant`, `ApAddress`, `Respondent`, `CaseInfo`, `Section`, `Hash1`, `Hash2`) VALUES
(1, 'jack', '1259', 'FIR145', '2025-03-01', 'Jack', 'Trichy', 'Guna', 'murder', 189, '0', '01A13732E65EF997DE8A960740AB4E96E13FF5A64BA41EC98E7ED1E4ABC0E58F');

-- --------------------------------------------------------

--
-- Table structure for table `noctb`
--

CREATE TABLE `noctb` (
  `nid` bigint(250) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Address` varchar(250) NOT NULL,
  `Date` varchar(250) NOT NULL,
  `Oname` varchar(250) NOT NULL,
  `Status` varchar(250) NOT NULL,
  `Document` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  PRIMARY KEY  (`nid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `noctb`
--

INSERT INTO `noctb` (`nid`, `Name`, `Address`, `Date`, `Oname`, `Status`, `Document`, `UserName`) VALUES
(1, 'mark', 'Trichy', '2025-03-06', 'ibbu', 'Rejected', '', 'mark'),
(2, 'mark', 'Trichy', '2025-03-06', 'ibbu', 'Approved', 'gettyimages-128502214-612x612.jpg', 'mark'),
(3, 'raghul', 'Trichy', '2025-03-07', 'ibbu', 'Approved', 'maran poster.jpeg', 'raghul');

-- --------------------------------------------------------

--
-- Table structure for table `regtb`
--

CREATE TABLE `regtb` (
  `id` bigint(20) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `Designation` varchar(250) NOT NULL,
  `StationNo` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `regtb`
--

INSERT INTO `regtb` (`id`, `Name`, `Mobile`, `Email`, `Address`, `Designation`, `StationNo`, `UserName`, `Password`) VALUES
(1, 'mark', '9896959545', 'javaprojectfantasy@gmail.com', 'Trichy', 'Inspector', '123', 'mark', 'mark'),
(2, 'jack', '9694563515', 'javaprojectfantasy@gmail.com', 'Trichy', 'Inspector', '1259', 'jack', 'jack');

-- --------------------------------------------------------

--
-- Table structure for table `usertb`
--

CREATE TABLE `usertb` (
  `id` bigint(20) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `usertb`
--

INSERT INTO `usertb` (`id`, `Name`, `Mobile`, `Email`, `Address`, `UserName`, `Password`) VALUES
(1, 'mark', '9896959545', 'javaprojectfantasy@gmail.com', 'trichy', 'mark', 'mark'),
(2, 'raghul', '9896959545', 'javaprojectfantasy@gmail.com', 'Trichy', 'raghul', 'raghul');
