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

import java.util.ArrayList;

public class BufferedRecordMesgBroadcaster implements RecordMesgListener{
    private BufferedRecordMesg bufferedRecordMesg;
    private ArrayList<BufferedRecordMesgListener> listeners;

    public BufferedRecordMesgBroadcaster() {
        bufferedRecordMesg = new BufferedRecordMesg();
        listeners = new ArrayList<BufferedRecordMesgListener>();
    }

    public void addListener(BufferedRecordMesgListener mesgListener) {
        listeners.add(mesgListener);
    }

    public void removeListener(BufferedRecordMesgListener mesgListener) {
        listeners.remove(mesgListener);
    }

    public void onMesg(final RecordMesg mesg) {
        bufferedRecordMesg.setFields(mesg);

        for (final BufferedRecordMesgListener listener : listeners) {
            listener.onMesg(bufferedRecordMesg);
        }
    }
}
