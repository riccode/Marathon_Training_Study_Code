////////////////////////////////////////////////////////////////////////////////
// The following FIT Protocol software provided may be used with FIT protocol
// devices only and remains the copyrighted property of Dynastream Innovations Inc.
// The software is being provided on an "as-is" basis and as an accommodation,
// and therefore all warranties, representations, or guarantees of any kind
// (whether express, implied or statutory) including, without limitation,
// warranties of merchantability, non-infringement, or fitness for a particular
// purpose, are specifically disclaimed.
//
// Copyright 2018 Dynastream Innovations Inc.
////////////////////////////////////////////////////////////////////////////////
// ****WARNING****  This file is auto-generated!  Do NOT edit this file.
// Profile Version = 20.66Release
// Tag = production/akw/20.66.00-0-gc7b345b
////////////////////////////////////////////////////////////////////////////////


package com.garmin.fit;

import java.util.HashMap;
import java.util.Map;

public class SportBits2 {
    public static final short MOUNTAINEERING = 0x01;
    public static final short HIKING = 0x02;
    public static final short MULTISPORT = 0x04;
    public static final short PADDLING = 0x08;
    public static final short FLYING = 0x10;
    public static final short E_BIKING = 0x20;
    public static final short MOTORCYCLING = 0x40;
    public static final short BOATING = 0x80;
    public static final short INVALID = Fit.UINT8Z_INVALID;

    private static final Map<Short, String> stringMap;

    static {
        stringMap = new HashMap<Short, String>();
        stringMap.put(MOUNTAINEERING, "MOUNTAINEERING");
        stringMap.put(HIKING, "HIKING");
        stringMap.put(MULTISPORT, "MULTISPORT");
        stringMap.put(PADDLING, "PADDLING");
        stringMap.put(FLYING, "FLYING");
        stringMap.put(E_BIKING, "E_BIKING");
        stringMap.put(MOTORCYCLING, "MOTORCYCLING");
        stringMap.put(BOATING, "BOATING");
    }


    /**
     * Retrieves the String Representation of the Value
     * @return The string representation of the value, or empty if unknown
     */
    public static String getStringFromValue( Short value ) {
        if( stringMap.containsKey( value ) ) {
            return stringMap.get( value );
        }

        return "";
    }

    /**
     * Retrieves a value given a string representation
     * @return The value or INVALID if unkwown
     */
    public static Short getValueFromString( String value ) {
        for( Map.Entry<Short, String> entry : stringMap.entrySet() ) {
            if( entry.getValue().equals( value ) ) {
                return entry.getKey();
            }
        }

        return INVALID;
    }

}
