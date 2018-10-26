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

public class CourseCapabilities {
    public static final long PROCESSED = 0x00000001;
    public static final long VALID = 0x00000002;
    public static final long TIME = 0x00000004;
    public static final long DISTANCE = 0x00000008;
    public static final long POSITION = 0x00000010;
    public static final long HEART_RATE = 0x00000020;
    public static final long POWER = 0x00000040;
    public static final long CADENCE = 0x00000080;
    public static final long TRAINING = 0x00000100;
    public static final long NAVIGATION = 0x00000200;
    public static final long BIKEWAY = 0x00000400;
    public static final long INVALID = Fit.UINT32Z_INVALID;

    private static final Map<Long, String> stringMap;

    static {
        stringMap = new HashMap<Long, String>();
        stringMap.put(PROCESSED, "PROCESSED");
        stringMap.put(VALID, "VALID");
        stringMap.put(TIME, "TIME");
        stringMap.put(DISTANCE, "DISTANCE");
        stringMap.put(POSITION, "POSITION");
        stringMap.put(HEART_RATE, "HEART_RATE");
        stringMap.put(POWER, "POWER");
        stringMap.put(CADENCE, "CADENCE");
        stringMap.put(TRAINING, "TRAINING");
        stringMap.put(NAVIGATION, "NAVIGATION");
        stringMap.put(BIKEWAY, "BIKEWAY");
    }


    /**
     * Retrieves the String Representation of the Value
     * @return The string representation of the value, or empty if unknown
     */
    public static String getStringFromValue( Long value ) {
        if( stringMap.containsKey( value ) ) {
            return stringMap.get( value );
        }

        return "";
    }

    /**
     * Retrieves a value given a string representation
     * @return The value or INVALID if unkwown
     */
    public static Long getValueFromString( String value ) {
        for( Map.Entry<Long, String> entry : stringMap.entrySet() ) {
            if( entry.getValue().equals( value ) ) {
                return entry.getKey();
            }
        }

        return INVALID;
    }

}
